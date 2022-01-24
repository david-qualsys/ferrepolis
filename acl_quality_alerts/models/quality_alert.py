from odoo import models, fields


class QualityAlert(models.Model):
    _inherit = 'quality.alert'

    saleorder_id = fields.Many2one('sale.order', string='Orden de Venta', domain=['&', ('state', '!=', 'draft'), ('state', '!=', 'cancel')])
