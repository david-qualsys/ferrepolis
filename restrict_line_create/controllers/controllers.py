# -*- coding: utf-8 -*-
from odoo import http

# class FieldsFaly(http.Controller):
#     @http.route('/fields_faly/fields_faly/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fields_faly/fields_faly/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fields_faly.listing', {
#             'root': '/fields_faly/fields_faly',
#             'objects': http.request.env['fields_faly.fields_faly'].search([]),
#         })

#     @http.route('/fields_faly/fields_faly/objects/<model("fields_faly.fields_faly"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fields_faly.object', {
#             'object': obj
#         })