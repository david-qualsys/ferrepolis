from odoo import tools

from odoo.tools.translate import _
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    opportunity_id = fields.Many2one('crm.lead', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', True)], 'sale': [('readonly', True)], 'cancel': [('readonly', True)]})
    medium_id = fields.Many2one('utm.medium', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', True)], 'sale': [('readonly', True)], 'cancel': [('readonly', True)]})
    campaign_id = fields.Many2one('utm.campaign', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', True)], 'sale': [('readonly', True)], 'cancel': [('readonly', True)]})
    tag_ids = fields.Many2many('crm.lead.tag', 'sale_order_tag_rel', 'order_id', 'tag_id', string='Tags', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', True)], 'sale': [('readonly', True)], 'cancel': [('readonly', True)]})
    #source_id = fields.One2many('utm.source', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', True)], 'sale': [('readonly', True)], 'cancel': [('readonly', True)]})




   