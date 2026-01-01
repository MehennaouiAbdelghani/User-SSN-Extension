{
    'name': 'User SSN Extension',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Add Social Security Number field to Users',
    'description': """
        This module adds a Social Security Number (SSN) field to the User model.
        Features:
        - Adds SSN field to user form (after Name field)
        - Adds SSN field to user tree/list view
        - Validates SSN format (exactly 12 digits)
        - Provides masked input for better UX
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'views/user_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}