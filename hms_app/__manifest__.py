{
    'name': "HMS App",
    'summary': """ """,
    'description': """ """,
    'author': "Mostafa Hassan",
    'category': 'Productivity',
    'version': '17.0.0.1.0',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/base_menus.xml',
        'views/patient_view.xml',
        'views/department_view.xml',
        'views/doctor_view.xml',
        'wizard/add_patient_wizard.xml',
    ],
}
