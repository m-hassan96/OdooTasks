from odoo import fields, models


class Doctor(models.Model):
    _name = 'hms.doctor'
    _description = 'Doctor'
    _rec_name = 'f_name'

    f_name = fields.Char('First Name', required=True)
    l_name = fields.Char('Last Name', required=True)
    image = fields.Binary()
    department_id = fields.Many2one('hms.department', required=True)
    Patients_id = fields.One2many('hms.patient', 'doctor_id')
