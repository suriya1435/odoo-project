from odoo import models , fields ,api


class Student(models.Model):
    _name='student.arch'
    _description="to build an student data module"
    

    partner_id = fields.Many2one('res.partner' , string = "Student Name" , required = True)
    age = fields.Integer(string = "Age")



