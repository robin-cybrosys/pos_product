from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'

    location_id = fields.Many2one(
        'stock.location', 'Location',
        help='If left empty, availability won\'t be checked')

    @api.onchange('location_id')
    def change(self):
        print(self.location_id.quant_ids.product_id)
