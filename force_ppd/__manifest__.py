# -*- coding: utf-8 -*-
{
    'name': "Force PPD",

    'summary': """
        Force PPD on Invoice""",

    'description': """
        Force PPD on Invoice 
    """,

    'author': "Qualsys consulting",
    'website': "http://www.qualsys.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Account Invoice',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'l10n_mx_edi','account_accountant'],

    # always loaded
    'data': [
        'views/account_invoice.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
