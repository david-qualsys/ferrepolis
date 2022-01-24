# -*- coding: utf-8 -*-

from odoo import models, fields, api

class saleOrder(models.Model):

	_inherit = "stock.picking"

	re_req = fields.Char(string="Requisición")


