from odoo import fields, models, api

AVAILABLE_PRIORITIES = [
    ('0', 'Nil'),
    ('1', 'Normal'),
    ('2', 'Average'),
    ('3', 'Good'),
    ('4', 'Very Good'),
    ('5', 'Excellent'),
]


class Product(models.Model):
    _inherit = ['product.template']
    grade = fields.Char(string="Grade")
    rating = fields.Selection(AVAILABLE_PRIORITIES, default='0')

    @api.onchange('rating')
    def change(self):
        print(self.rating)

