{
    'name': 'GBD CRM',
    'description': 'CRM Customizations for specificaly Walton Global Business',
    'summary': 'All the customization required that is changing the standard business logic for odoo for Walton Global Business is done here.',
    'version': '16.0.1.0.0',
    'category': 'Tools',
    'author': 'K. M. JIAUL ISLAM',
    'maintainer': 'WALTON DIGI-TECH INDUSTRIES LTD.',
    'website': 'https://www.waltondigitech.com/',
    'depends': ['base', 'sale', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/sale_order.xml',
        'views/ir_sequence.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
