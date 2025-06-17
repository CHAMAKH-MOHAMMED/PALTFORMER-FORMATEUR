{
    'name': 'Academy Trainers Management',
    'version': '17.0.1.0.0',
    'summary': 'Manage trainer profiles, CVs, and allow training centers to search for trainers.',
    'description': """
        This module provides a platform for trainers to showcase their profiles and CVs,
        and for training centers to find suitable trainers based on various criteria.
    """,
    'author': 'Jules Agent',
    'website': 'https://www.example.com', # Placeholder website
    'category': 'Website/Training',
    'depends': ['base', 'website', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'views/website_menus.xml',
        'views/templates_trainers_list.xml',
        'views/templates_trainer_profile.xml',
        'views/templates_trainer_form.xml',
        'views/templates_trainer_search.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
