from odoo import models, fields, api


class HotelSalesReport(models.TransientModel):
    _name = 'hotel.sales.report'
    _description = 'Hotel Sales Report'

    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')

    total_sales = fields.Float(string='Total Sales', readonly=True)
    total_orders = fields.Integer(string='Total Orders', readonly=True)

    def generate_report(self):
        bills = self.env['hotel.bill'].search([
            ('bill_date', '>=', self.from_date),
            ('bill_date', '<=', self.to_date)
        ])

        self.total_sales = sum(bills.mapped('total_amount'))
        self.total_orders = len(bills)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'hotel.sales.report',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }