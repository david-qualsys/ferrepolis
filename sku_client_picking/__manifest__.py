# -*- coding: utf-8 -*-
{
    'name': "SKU Client on Picking",

    'summary': """
        Add SKU client on stock picking orders""",

    'description': """
        Add SKU client on stock picking orders
    """,

    'author': "Qualsys Consulting SC",
    'website': "http://www.qualsys.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        'views/stock_picking.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}