from odoo import api, SUPERUSER_ID
from . import models
from . import controllers

def sample_data(env):
    env['product.category'].create_car_categories()
