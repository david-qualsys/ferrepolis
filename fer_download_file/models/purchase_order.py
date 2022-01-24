from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError
from lxml import etree
import base64

import logging
_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model): 
    _inherit = "purchase.order"

    test_txt = fields.Binary(string='Archivo prueba txt')

    def download_file(self):
        self.state='sent'
        nombre="Solicitud"+self.name+".txt"
        # ruta ="/odoo14hd/odoo14hd-server/Odoo_14hd/" + nombre
        # ruta ="/odoo/odoo-server/" + nombre
        data = open(nombre,'w+')
        data.write("%s \r\n" % self.partner_id.ref)
        for line in self.order_line:
            data.write("%s,%d\r\n" % (line.product_id.default_code,int(line.product_qty)))
        file_data = data.read()
        # data.close()
        self.test_txt = base64.b64encode(open(nombre, "rb").read())

        values = {
                    'name': nombre,
                    # 'datas_fname': nombre,
                    'res_model': 'purchase.order',
                    'res_id': self.id,
                    'type': 'binary',
                    'public': True,
                    'datas': base64.b64encode(open(nombre, "rb").read()),
                    # 'datas': file_data.encode('utf8').encode('base64'),
                }

        attachment_id = self.env['ir.attachment'].sudo().create(values)
        download_url = '/web/content/attachment_id=' + str(attachment_id.id) + '?download=True'
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')


        return {
                'type': 'ir.actions.act_url',
                'url': '/web/content/%s?download=true' % (attachment_id.id),
                'target': 'new',
                'nodestroy': False,
                # "context": self.env.context,
                # "type": "ir.actions.report",
                # "data": file_data,
                # "res_id": attachment_id.id,
                # "res_model": "ir.attachment",
                # "target": "new",
        }
        # return {
        #     'type': 'ir.actions.act_url',
        #     'name': 'contract',
        #     'url': '/web/content/purchase.order/%s/test_txt/%s?download=true' %(self.id,nombre),
        # }
        # f_read = Your test file # Test file 
        # file_data = f_read.read()
        #Pass your text file data using encoding.
        # Using your data create as attachment
        # attachment_id = self.env['ir.attachment'].sudo().create(values)
        #Prepare your download URL
        # download_url = '/web/content/' + str(\attachment_id.id) + '?download=True'
        # base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        # Return so it will download in your system
        # return {
        #         "type": "ir.actions.act_url",
        #         "url": str(base_url)  +  str(download_url),
        #         "target": "new",
        # }
