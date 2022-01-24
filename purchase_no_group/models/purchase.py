# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _make_po_get_domain(self, values, partner):
        domain = super(StockRule, self)._make_po_get_domain(values, partner)
        domain += (('origin', 'ilike', values['move_dest_ids'][0].origin or false),)
            
        return domain


