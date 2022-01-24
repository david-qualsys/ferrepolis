# -*- coding: utf-8 -*-
{
    'name': "Adición de campos de ventas en Alertas de calidad",
    'summary': """
        Agrega campos de ventas en Quality Alert
        """,
    'description': """
        Este desarrollo facilita la adicion de ventas en de facturas a ordenes de compra.
    """,
    'author': "Qualsys Consulting",
    'website': "https://www.qualsys.com.mx",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Account',
    'version': '14.0.1',
    # any module necessary for this one to work correctly
    'depends': ['account', 'sale'],
    # always loaded
    'data': [
        'views/quality_alert_views_inherit.xml'
        ],
    'qweb': [],
    # only loaded in demonstration mode
    'demo': [],
}