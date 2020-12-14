from dateutil.relativedelta import relativedelta
from odoo import api,fields,models

from odoo_14e.odoo.fields import Datetime


class Student(models.Model):
    _name = 'student.info'

    f_name = fields.Char(string="First Name", required=True)
    l_name = fields.Char(string="Last Name", required=True)
    full_name = fields.Char(string="Full Name", compute='get_fullname',store=True)
    rollno = fields.Integer(String="Roll No")
    gender=fields.Selection([('M','Male'),('F','Female')],String="Gender")
    dob = fields.Date("Date Of Birth")
    age = fields.Integer(String="Age", compute='calculate_age', store=True)
    phone = fields.Char(string="Phone No")
    email = fields.Char(string="Email")

    hobbies_ids = fields.One2many('student.hobbies', 'student_id', string="Hobbies")

    @api.depends('dob')
    def calculate_age(self):
        for record in self:
            age_vlaue = relativedelta(Datetime.now().date(), fields.Datetime.from_string(record.dob)).years
            record.age = age_vlaue

    @api.depends('f_name','l_name')
    def get_fullname(self):
        for record in self:
            if record.f_name:
                if record.l_name:
                    fullname = record.f_name + ' ' + record.l_name
                    record.full_name = fullname

class Hobbies(models.Model):
    _name = 'student.hobbies'

    student_id = fields.Many2one('student.info', string='Student', required=True)
    reading = fields.Boolean(string="Reading")
    swimming = fields.Boolean(string="Swimming")
    dancing = fields.Boolean(string="Dancing")