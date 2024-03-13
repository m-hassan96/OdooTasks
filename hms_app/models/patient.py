from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
import re


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'
    _rec_name = 'f_name'
    _sql_constraints = [
        ('unique_email', 'unique("email")', 'This Email is exist!')
    ]

    f_name = fields.Char('First Name', required=True)
    l_name = fields.Char('Last Name', required=True)
    birth_date = fields.Date('Birth Date')
    age = fields.Integer(compute='_compute_age')
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
    department_id = fields.Many2one('hms.department')
    doctor_id = fields.Many2one('hms.doctor')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('serious', 'Serious'),
        ('fair', 'Fair'),
        ('good', 'Good'),
    ])
    email = fields.Char(required=True)
    department_capacity = fields.Integer(related='department_id.capacity')
    line_ids = fields.One2many('hms.patient.line', 'patient_id')

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                rec.age = relativedelta(fields.Date.today(), rec.birth_date).years
            else:
                rec.age = False

    @api.constrains('email')
    def _check_email_vali(self):
        for rec in self:
            patient_email = self.env['hms.patient'].search([('email', '=', rec.email), ('id', '!=', rec.id)])
            if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email):
                raise UserError("This Email not valid please insert it again")
            if patient_email:
                raise UserError("This Email already exist.")

    def action_undetermined(self):
        for rec in self:
            rec.state = 'undetermined'

    def action_good(self):
        for rec in self:
            rec.state = 'good'

    def action_fair(self):
        for rec in self:
            rec.state = 'fair'

    def action_serious(self):
        for rec in self:
            rec.state = 'serious'

    def action_add_log(self):
        action = self.env['ir.actions.actions']._for_xml_id('hms_app.patient_wizard_action')
        action['context'] = {
            'default_patient_id': self.id,
        }
        return action

    class PatientLine(models.Model):
        _name = 'hms.patient.line'
        _description = 'Patient Line'

        patient_id = fields.Many2one('hms.patient', readonly="1")
        created_by = fields.Char(default=lambda self: self.env.user.name, readonly="1")
        date = fields.Date(default=fields.Date.today, readonly="1")
        description = fields.Text(required=True)
        patient_logs = fields.Many2one('hms.patient')

    @api.onchange('age')
    def _on_change_pcr(self):
        for record in self:
            if record.age < 30 and self.age != 0:
                record.pcr = True
                return {
                    'warning': {'title': "Your age is lower than 30 Year",
                                'message': "The PCR has checked"},
                }
            else:
                record.pcr = False
