from odoo import models, fields

class Person(models.Model):
    _name = 'person.info'
    _description = 'Person Information'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')