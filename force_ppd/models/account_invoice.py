# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

        
    @api.multi
    def _l10n_mx_edi_get_payment_policy(self):
        self.ensure_one()
        version = self.l10n_mx_edi_get_pac_version()
        term_ids = self.payment_term_id.line_ids
        days = self.payment_term_id.line_ids[0].days
        if version == '3.2':
            if len(term_ids.ids) > 1:
                return 'Pago en parcialidades'
            else:
                return 'Pago en una sola exhibición'
        elif version == '3.3' and self.date_due and self.date_invoice:
            # In CFDI 3.3 - SAT 2018 rule 2.7.1.44, the payment policy is PUE
            # if the invoice will be paid before 17th of the following month,
            # PPD otherwise
            #date_pue = fields.Date.from_string(self.date_pue)#.from_string(self.date_invoice) +
                        #relativedelta(day=17, months=1))
            #date_due = fields.Date.from_string(self.date_due)
            if ( days > 1):
                return 'PPD'
            return 'PUE'
        return ''
        return super(AccountInvoice, self)._l10n_mx_edi_get_payment_policy()
