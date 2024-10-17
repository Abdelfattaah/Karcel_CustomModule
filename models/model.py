from odoo import models, fields, api

class ProductCategorySetup(models.Model):
    _inherit = 'product.category'



    @api.model
    def create_car_categories(self):
        cars_category = self.env['product.category'].search([('name', '=', 'Cars')], limit=1)

        if not cars_category:
            cars_category = self.env['product.category'].create({'name': 'Cars'})
        else:
            return

        subcategories = {
            'Kia': ['Cerato', 'Carens'],
            'Nissan': ['Sunny', 'Sentra'],
            'Hyundai': ['Elantra', 'Tucson'],
        }

        for brand, models in subcategories.items():

            brand_category = self.env['product.category'].create({'name': brand, 'parent_id': cars_category.id})

            for model in models:
                    self.env['product.category'].create({'name': model, 'parent_id': brand_category.id})