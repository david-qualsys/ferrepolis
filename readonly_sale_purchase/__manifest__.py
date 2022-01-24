# -*- coding: utf-8 -*-
{
    'name': "ACL-SALE-PURCHASE Readonly",

    'summary': """
        Solo lectura en pedidos de Ventas / Compras""",

    'description': """
    """,

    'author': "Qualsys Consulting SC",
    'website': "http://www.qualsys.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management','purchase'],

    # always loaded
    'data': [
        'views/sale_order.xml',
        'views/purchase_order.xml',
        #'views/sale.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
