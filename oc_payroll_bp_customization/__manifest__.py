# -*- coding: utf-8 -*-
{
    'name': "BroadPeak Customizations",

    'summary': """
        This module contains custom development of Broadpeak""",

    'description': """
        This module contains custom development of Broadpeak. Its mainly customization related to
        HR
    """,

    'author': "OdooConcepts",
    'website': "http://www.odooconcepts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
}
