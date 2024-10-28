
{
    'name' : 'Android MDM',
    'version':'1.0',
    'category': 'Tools',
    'summary': 'Mobile Device Management System for Android',
    'author': 'Habib',
    'depends': ['base', 'web'],
    'data': [
'security/ir.model.access.csv'
'views/mdm_actions.xml',
'views/menu_view.xml',
'views/device_views.xml',
'views/policy_views.xml',
'views/app_views.xml',

],
'installable': True,
'application': True
}
