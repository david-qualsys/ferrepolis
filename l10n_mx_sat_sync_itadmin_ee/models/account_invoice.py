# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64

DEFAULT_CFDI_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
        
    attachment_id = fields.Many2one("ir.attachment", 'Attachment')
    l10n_mx_edi_cfdi_xml = fields.Binary('XML')
    l10n_mx_edi_cfdi_uuid_cusom = fields.Char(string='Fiscal Folio UUID', copy=False, readonly=True)#, compute="_compute_cfdi_uuid", store=True)
    
    @api.multi
    @api.depends('l10n_mx_edi_cfdi_name')
    def _compute_cfdi_uuid(self):
        for inv in self:
            attachment_id = inv.l10n_mx_edi_retrieve_last_attachment()
            if not attachment_id:
                inv.l10n_mx_edi_cfdi_uuid_cusom=False
            else:
                datas = attachment_id._file_read(attachment_id.store_fname)
                
                tree = inv.l10n_mx_edi_get_xml_etree(base64.decodestring(datas))
                # if already signed, extract uuid
                tfd_node = inv.l10n_mx_edi_get_tfd_etree(tree)
                if tfd_node is not None:
                    inv.l10n_mx_edi_cfdi_uuid_cusom = tfd_node.get('UUID')
    
    
