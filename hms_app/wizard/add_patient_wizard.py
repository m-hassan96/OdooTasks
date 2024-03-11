from odoo import models, fields


class AddLog(models.TransientModel):
    _name = 'patient.wizard'
    _description = 'Add Patient History'

    patient_id = fields.Many2one('hms.patient', readonly="1")
    log_id = fields.Many2one('hms.patient.line')
    created_by = fields.Char("Created by", default=lambda self: self.env.user.name , readonly="1")
    date = fields.Date(default=fields.Date.today(), readonly="1")
    description = fields.Text(required=True)

    def action_add_log(self):
        self.env['hms.patient.line'].create({
            'patient_id': self.patient_id.id,
            'description': self.description
        })
