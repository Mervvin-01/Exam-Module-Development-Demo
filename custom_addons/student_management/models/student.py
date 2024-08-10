from odoo import fields, models, api, _


class Student(models.Model):
    _name = "student"

    name = fields.Char()
    phone = fields.Char()
    address = fields.Text()
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    state = fields.Many2one('res.country.state', 'Fed. State', domain="[('country_id', '=?', country)]")
    country = fields.Many2one('res.country')
    email = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")
    grade = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('f', 'F'),
    ], string="Grade")
    user_id = fields.Many2one('res.users')

    def create_user(self):
        for record in self:
            user = self.env['res.users']
            user_id = user.sudo().create({
                'name': record.name,
                'login': record.email,
                'is_student': True,
            })
            record.user_id = user_id.id





