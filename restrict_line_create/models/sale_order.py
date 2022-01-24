from odoo import tools

from odoo.tools.translate import _
from odoo.osv.orm import except_orm
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account', readonly=True, required=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)], 'cancel': [('required', False)], 'sale': [('required', False)]}, help="The analytic account related to a sales order.", copy=False, oldname='project_id')

