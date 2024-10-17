import logging
from odoo import http
from odoo.http import request

class FilterCars(http.Controller):

    @http.route('/', auth='public', website=True)
    def filter_home(self, **kw):

        cars_category = http.request.env['product.category'].search([('name', '=', 'Cars')], limit=1)
        children_categories = cars_category.child_id


        brand_models_dict = {}
        for brand in children_categories:

            car_models = brand.child_id
            brand_models_dict[brand] = car_models

        products = http.request.env['product.template'].search([('categ_id', 'child_of', cars_category.id)])


        return request.render(
            'karcel_task.template_find_car',{
                'brand_models_dict': brand_models_dict,
                'products': products,

            })

    @http.route('/apply_filter', auth='public', type="http", methods=["GET"], website=True)
    def apply_filter(self, **kw):

        model_ids = []
        brand_ids = []
        filter_string = kw.get('selected_data')

        if filter_string:
            params = filter_string.split('&')
            for param in params:
                key, value = param.split('=')
                if key == 'model':
                    model_ids.append(int(value))
                elif key == 'brand':
                    brand_ids.append(int(value))

        cars_category = request.env['product.category'].search([('name', '=', 'Cars')], limit=1)
        domain = [('categ_id', 'child_of', cars_category.id)]

        if model_ids:
            domain.append(('categ_id', 'in', model_ids))

        if brand_ids:
            domain.append(('categ_id.parent_id', 'in', brand_ids))

        products = request.env['product.product'].search(domain)

        cars_category = request.env['product.category'].search([('name', '=', 'Cars')], limit=1)
        brand_models_dict = {}
        if cars_category:
            for brand in cars_category.child_id:
                brand_models_dict[brand] = brand.child_id

        return request.render(
            'karcel_task.template_find_car',
            {
                'brand_models_dict': brand_models_dict,
                'products': products,
            }
        )