# -*- coding: utf-8 -*-
{
    'name': "Descarga de arhcivo",

    'summary': """
        Permite descargar archivos
        """,

    'description': """
        Este desarrollo permite descargar archivos.
    """,

    'author': "Qualsys Consulting",
    'website': "https://www.qualsys.com.mx",

    'category': 'Purchase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 
                'purchase', 
                'sale', 
                'stock',
                'account',
                ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/file_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
