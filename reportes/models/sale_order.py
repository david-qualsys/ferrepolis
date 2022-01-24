# -*- coding: utf-8 -*-

from odoo import models, fields, api

class saleOrder(models.Model):

	_inherit = "sale.order"

	analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account',readonly=False, required=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)], 'sale': [('readonly', False)]}, help="The analytic account related to a sales order.", copy=False, oldname='project_id')


