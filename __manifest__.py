{
    'name': 'Office Requests',
    'version': '1.0.0',
    'summary': 'Make office request',
    'description': """
        Office Requests is an Odoo App blana dkdkdk a djdkd
    """,
    'author': 'Akinshola Samuel',
    'category': 'Tools,Office',
    "license": 'LGPL-3',
    'website': 'akinshola.com',
    'depends': ['base', 'hr'],
    'data': [
        'security/security.xml',
        'views/views.xml',
        'views/actions.xml',
        'menus/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}