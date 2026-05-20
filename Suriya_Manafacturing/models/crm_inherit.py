from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    steel_order_count = fields.Integer(compute='_compute_steel_order_count')

    def _compute_steel_order_count(self):
        for rec in self:
            rec.steel_order_count = self.env['steel.order'].search_count([
                ('lead_id', '=', rec.id)
            ])