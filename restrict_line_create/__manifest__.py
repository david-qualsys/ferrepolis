# -*- coding: utf-8 -*-
{
    'name': "Restrict Line Create",

    'summary': """
        Restringe la creación desde lineas de pedido""",

    'description': """
    """,

    'author': "Qualsys Consulting SC",
    'website': "http://www.qualsys.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'contacts', 'account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_lost.xml',
        'views/sale_order.xml',
        #'views/res_partner.xml',
        'views/purchase_order.xml',
        #'views/account_invoice.xml',
        #'views/account_journal.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
