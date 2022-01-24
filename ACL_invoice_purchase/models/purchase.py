# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    #l10n_mx_edi_cfdi_uuid_cusom = fields.Char(string='Fiscal Folio UUID', copy=True, readonly=True)


    @api.multi
    def action_view_invoice(self):
        '''
        This function returns an action that display existing vendor bills of given purchase order ids.
        When only one found, show the vendor bill immediately.
        '''
        action = self.env.ref('account.action_vendor_bill_template')
        result = action.read()[0]
        create_bill = self.env.context.get('create_bill', False)
        # override the context to get rid of the default filtering
        result['context'] = {
            'type': 'in_invoice',
            'default_purchase_id': self.id,
            'default_currency_id': self.currency_id.id,
            'default_company_id': self.company_id.id,
            'company_id': self.company_id.id
        }
        # choose the view_mode accordingly
        if len(self.invoice_ids) > 1 and not create_bill:
            result['domain'] = "[('id', 'in', " + str(self.invoice_ids.ids) + ")]"
        else:
            res = self.env.ref('account.invoice_supplier_form', False)
            result['views'] = [(res and res.id or False, 'form')]
            # Do not set an invoice_id if we want to create a new bill.
            if not create_bill:
                result['res_id'] = self.invoice_ids.id or False
        result['context']['default_origin'] = self.name
        result['context']['default_reference'] = self.partner_ref
        result['context']['default_l10n_mx_edi_cfdi_uuid_cusom'] = self.l10n_mx_edi_cfdi_uuid_cusom
        result['context']['default_l10n_mx_edi_cfdi_xml'] = self.l10n_mx_edi_cfdi_name
        return result
        return super(PurchaseOrder,self).action_view_invoice(result)
