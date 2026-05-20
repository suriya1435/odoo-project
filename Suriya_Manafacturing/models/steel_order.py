from odoo import models, fields, api

class SteelOrder(models.Model):
    _name = 'steel.order'
    _description = 'Steel Order'

    name = fields.Char(required=True)
    sale_id = fields.Many2one('sale.order')
    lead_id = fields.Many2one('crm.lead')
    customer_id = fields.Many2one('res.partner')
    product_id = fields.Many2one('product.product')
    process_line_ids = fields.One2many('steel.process.line', 'order_id')

    total_cost = fields.Float(string="Total Cost", compute="_compute_total", store=True)
    total_scrap_qty = fields.Float(compute="_compute_total", store=True)
    total_scrap_value = fields.Float(compute="_compute_total", store=True)
    net_cost = fields.Float(compute="_compute_net_cost", store=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('process', 'Processing'),
        ('done', 'Done'),
    ], default="draft")

    @api.depends(
        'process_line_ids.cost',
        'process_line_ids.scrap_qty',
        'process_line_ids.scrap_value',
    )
    def _compute_total(self):
        for rec in self:
            rec.total_cost = sum(line.cost for line in rec.process_line_ids)
            rec.total_scrap_qty = sum(line.scrap_qty for line in rec.process_line_ids)
            rec.total_scrap_value = sum(line.scrap_value for line in rec.process_line_ids)

    @api.depends('total_cost', 'total_scrap_value')
    def _compute_net_cost(self):
        for rec in self:
            rec.net_cost = rec.total_cost - rec.total_scrap_value


    def action_start(self):
    	for rec in self:
        	rec.state = 'process'

    def action_done(self):
     	for rec in self:
        	rec.state = 'done'