from odoo import fields, models


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'
    _rec_name = 'f_name'

    f_name = fields.Char('First Name', required=True)
    l_name = fields.Char('Last Name', required=True)
    birth_date = fields.Date('Birth Date')
    age = fields.Integer()
    address = fields.Char()
    history = fields.Html()
    pcr = fields.Boolean('PCR')
    cr_ratio = fields.Float('CR Ratio')
    blood_type = fields.Selection([
        ('group_A', 'Group A'),
        ('group_B', 'Group B'),
        ('group_O', 'Group O'),
        ('group_AB', 'Group AB'),
    ])
    image = fields.Binary()
    department_id = fields.Many2one('hms.department', required=True)
    doctor_id = fields.Many2one('hms.doctor', required=True)
    states = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ])
