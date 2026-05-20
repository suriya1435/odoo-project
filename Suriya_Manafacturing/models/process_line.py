from odoo import models, fields, api

class SteelProcessLine(models.Model):
    _name = "steel.process.line"
    _description = "Process Line"

    order_id = fields.Many2one("steel.order")

    process_type = fields.Selection([
        ('cutting', 'Cutting'),
        ('shaping', 'Shaping'),
        ('grinding', 'Grinding'),
        ('heating', 'Heating'),
        ('quenching', 'Quenching'),
        ('qc', 'Quality Check'),
        ('delivery', 'Delivery'),
    ])

    sequence = fields.Integer()
    location_type = fields.Selection([
        ('inhouse', 'In House'),
        ('outsourcing', 'Out Sourcing'),
    ])

    partner_id = fields.Many2one('res.partner')
    cost = fields.Float()

    scrap_qty = fields.Float()
    scrap_price = fields.Float()
    scrap_value = fields.Float(compute="_compute_scrap_value", store=True)

    @api.depends('scrap_qty', 'scrap_price')
    def _compute_scrap_value(self):
        for rec in self:
            rec.scrap_value = rec.scrap_qty * rec.scrap_price