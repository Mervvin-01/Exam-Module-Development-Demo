"""Module providing a functions related to Exam Center Management."""
from odoo import fields, models, api, _

class CenterManagement(models.Model):
    """Class for Center Management."""
    _name = "center.management"
    _description = "Center Management"
    _rec_name = "location"

    location = fields.Char()
    time_slots = fields.Selection([('morning', 'Morning'), ('afternoon', 'Afternoon')])
    available_seats = fields.Integer()
