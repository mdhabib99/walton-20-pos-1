from odoo import fields, models


class Student(models.Model):
    _name = 'edu.student'
    _description = "Student Model"

    name = fields.Char('student Name')
    email = fields.Char('E-mail Address')
    Mobile_number = fields.Char(string='Mobile Number')
    Designation = fields.Char('SR. DAD')

# class Students(models.Model):
#     _name = 'edu_ms'
#     _description = "Student Model"
#
#     name = fields.Char('student Name')
#     email = fields.Char('E-mail Address')
#
#
#     Mobile_number = fields.Char(string='Mobile Number')
#     Designation = fields.Char('SR. DAD')