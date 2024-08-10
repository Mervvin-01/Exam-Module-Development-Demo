
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ExamRegistration(models.Model):
    _name = "exam.registration"
    _description = "Students can register exams"

    name = fields.Char(default="New")
    stu_id = fields.Many2one('student', string="Student", readonly=True, default=lambda self: self._get_default_student())
    exam_id = fields.Many2one('exam', string="Exams")
    center_id = fields.Many2one('center.management', string="Exam Center")
    time_slots = fields.Selection([('morning', 'Morning'), ('afternoon', 'Afternoon')])
    date = fields.Date(compute="_compute_date_fee", store=True, default=False)
    exam_fee = fields.Float(compute="_compute_date_fee", store=True, default=0.0)
    status = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed')], default='draft')

    @api.depends('exam_id')
    def _compute_date_fee(self):
        for rec in self:
            if rec.exam_id:
                rec.date = rec.exam_id.date or False
                rec.exam_fee = rec.exam_id.exam_fee or 0
            else:
                rec.date = False
                rec.exam_fee = 0

    @api.model
    def _get_default_student(self):
        # Fetch the student associated with the current user
        return self.env['student'].search([('user_id', '=', self.env.uid)], limit=1)

    def action_confirm(self):
        for rec in self:
            if rec.status == 'draft':
                seat = rec.center_id.available_seats
                if seat > 0:
                    # Decrement available seats by 1
                    rec.center_id.write({'available_seats': seat - 1})
                    # Update the status to 'confirm'
                    rec.write({'status': 'confirm'})
                    # Generate reference number
                    rec.generate_reference_no()
                else:
                    raise ValidationError(_('No available seats at the selected center.'))
            else:
                raise ValidationError(_('Record should be in Draft stage.'))

    def generate_reference_no(self):
        if not self.name or self.name == 'New':
            self.name = self.env['ir.sequence'].next_by_code('exam_registration_sequence_code')

