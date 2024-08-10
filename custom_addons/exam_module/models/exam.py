"""Module providing a functions related to Exam Management."""
from datetime import datetime, timedelta, time
from odoo import fields, models, api, _


class Exam(models.Model):
    """Class for Exam Management."""
    _name = "exam"
    _description = "Exam"
    _rec_name = "title"

    title = fields.Char()
    description = fields.Text()
    date = fields.Date()
    duration = fields.Float()
    exam_fee = fields.Float()
    total_marks = fields.Integer()




