"""Module providing a functions related to Users."""
from odoo import fields, models


class Users(models.Model):
    """Class for Users."""
    _inherit = "res.users"

    is_student = fields.Boolean()

