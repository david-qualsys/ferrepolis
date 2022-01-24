from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)

class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    def cleaning_stock(self, id):
        # stock = self.sudo().browse(id)
        # stock.sudo().update({'company_id':1,'warehouse_id': 1})

        state_query = """
            UPDATE stock_picking_type SET company_id = 1,warehouse_id=1,sequence_id=NULL WHERE id = 11;
        """
        self._cr.execute(state_query)
