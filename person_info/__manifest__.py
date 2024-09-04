# __manifest__.py
{
    'name': 'Person Information',
    'version': '1.0',
    'summary': 'A module to manage person information',
    'description': """
        This module allows you to manage person information including name and age.
    """,
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
