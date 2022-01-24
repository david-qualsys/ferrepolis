# -*- coding: utf-8 -*-

from odoo import models, fields, api

class alumnos(models.Model):
    _inherit = 'stock.move'


    sku_client = fields.Char(String = 'Nombre', placeholder='Juanito Perez')




#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100