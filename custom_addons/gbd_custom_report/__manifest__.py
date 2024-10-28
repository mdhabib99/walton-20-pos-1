{
    'name': 'GBD Reports',
    'description': 'Module for report customization of GBD',
    'summary': 'A custom module for WALTON GB to meet their requirements for reports',
    'version': '16.0.1.0.0',
    'category': 'Report',
    'author': 'K. M. JIAUL ISLAM',
    'maintainer': 'WALTON DIGI-TECH INDUSTRIES LTD.',
    'website': 'https://www.waltondigitech.com/',
    'depends': ['base'],
    'data': [
        'reports/quotation_qweb_report.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'gbd_custom_report/static/src/scss/**/*'
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
