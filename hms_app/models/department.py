from odoo import fields, models


class Department(models.Model):
    _name = 'hms.department'
    _description = 'Department'

    name = fields.Char('Department Name', required=True)
    capacity = fields.Integer('Capacity', required=True)
    is_open = fields.Boolean('Is Open', required=True, default=True)
    doctors_id = fields.One2many('hms.doctor', 'department_id')
    Patients_id = fields.One2many('hms.patient', 'department_id')
