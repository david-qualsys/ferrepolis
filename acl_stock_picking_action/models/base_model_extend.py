# from odoo import api, models
# import logging
# from odoo.exceptions import UserError
# from odoo.tools.translate import _
# _logger = logging.getLogger(__name__)

# class BaseModelExtend(models.AbstractModel):
#     _inherit = 'base'

#     def _check_company(self, fnames=None):
#         # code
#         # return super(BaseModelExtend, self)._check_company(fnames)
#         if fnames is None:
#             fnames = self._fields

#         regular_fields = []
#         property_fields = []
#         for name in fnames:
#             field = self._fields[name]
#             if field.relational and field.check_company and \
#                     'company_id' in self.env[field.comodel_name]:
#                 if not field.company_dependent:
#                     regular_fields.append(name)
#                 else:
#                     property_fields.append(name)

#         if not (regular_fields or property_fields):
#             return

#         inconsistencies = []
#         _logger.info('######### self: %s',self)
#         _logger.info('######### stock_picking_type: %s',self)
#         for record in self:
#             _logger.info('######### record: %s',record)
#             company = record.company_id if record._name != 'res.company' else record
#             _logger.info('######### company: %s',company)
#             # The first part of the check verifies that all records linked via relation fields are compatible
#             # with the company of the origin document, i.e. `self.account_id.company_id == self.company_id`
#             _logger.info('######### regular_fields: %s',regular_fields)
#             for name in regular_fields:
#                 _logger.info('######### name: %s',name)
#                 corecord = record.sudo()[name]
#                 _logger.info('######### corecord: %s',corecord)
#                 if record._name=='stock.picking.type':
#                     _logger.info('######### dato: %s',record.default_location_src_id)
#                 # Special case with `res.users` since an user can belong to multiple companies.
#                 if corecord._name == 'res.users' and corecord.company_ids:
#                     if not (company <= corecord.company_ids):
#                         inconsistencies.append((record, name, corecord))
#                 elif not (corecord.company_id <= company):
#                     inconsistencies.append((record, name, corecord))
#                 _logger.info('############### inconsistencies: %s',inconsistencies)
#             # The second part of the check (for property / company-dependent fields) verifies that the records
#             # linked via those relation fields are compatible with the company that owns the property value, i.e.
#             # the company for which the value is being assigned, i.e:
#             #      `self.property_account_payable_id.company_id == self.env.company
#             company = self.env.company
#             for name in property_fields:
#                 # Special case with `res.users` since an user can belong to multiple companies.
#                 corecord = record.sudo()[name]
#                 if corecord._name == 'res.users' and corecord.company_ids:
#                     if not (company <= corecord.company_ids):
#                         inconsistencies.append((record, name, corecord))
#                 elif not (corecord.company_id <= company):
#                     inconsistencies.append((record, name, corecord))

#         if inconsistencies:
#             _logger.info('####################################### final inconsistencies: %s',inconsistencies)
#             lines = [_("Incompatible companies on records:")]
#             company_msg = _("- Record is company %(company)r and %(field)r (%(fname)s: %(values)s) belongs to another company.")
#             record_msg = _("- %(record)r belongs to company %(company)r and %(field)r (%(fname)s: %(values)s) belongs to another company.")
#             for record, name, corecords in inconsistencies[:5]:
#                 if record._name == 'res.company':
#                     msg, company = company_msg, record
#                 else:
#                     msg, company = record_msg, record.company_id
#                 field = self.env['ir.model.fields']._get(self._name, name)
#                 lines.append(msg % {
#                     'record': record.display_name,
#                     'company': company.display_name,
#                     'field': field.field_description,
#                     'fname': field.name,
#                     'values': ", ".join(repr(rec.display_name) for rec in corecords),
#                 })
#             raise UserError("\n".join(lines))
