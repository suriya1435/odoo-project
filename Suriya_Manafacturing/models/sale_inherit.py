from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            for line in order.order_line:
                self.env['steel.order'].create({
                    'name': order.name + "-" + line.product_id.name,
                    'sale_id': order.id,
                    'customer_id': order.partner_id.id,
                    'product_id': line.product_id.id,
                })
        return res