from odoo import fields, models


class Product(models.Model):
    _inherit = ['product.template']
    grade = fields.Char(string="Grade")

