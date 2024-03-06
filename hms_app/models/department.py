from odoo import fields, models


class Department(models.Model):
    _name = 'hms.department'
    _description = 'Department'

    name = fields.Char('Department Name', required=True)
    capacity = fields.Integer('Capacity', required=True)
    is_open = fields.Boolean('Is Open', required=True)
    Patients_id = fields.Many2one('hms.patient')
