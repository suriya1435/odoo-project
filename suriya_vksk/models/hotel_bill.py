from odoo import models, fields, api


class HotelBill(models.Model):
    _name = 'hotel.bill'
    _description = 'Hotel Bill'

    name = fields.Char(
        string='Bill Number',
        required=True,
        copy=False,
        readonly=True,
        default='New'
    )

    server_name = fields.Many2one(
        'res.partner',
        string='Server Name'
    )

    table_number = fields.Char(
        string='Table Number'
    )

    bill_date = fields.Datetime(
        string='Date',
        default=fields.Datetime.now
    )

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company
    )

    line_ids = fields.One2many(
        'hotel.bill.line',
        'bill_id',
        string='Food Items'
    )

    total_amount = fields.Float(
        string='Total Amount',
        compute='_compute_total',
        store=True
    )

    @api.depends('line_ids.subtotal')
    def _compute_total(self):
        for rec in self:
            rec.total_amount = sum(rec.line_ids.mapped('subtotal'))

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('hotel.bill') or 'New'

        return super(HotelBill, self).create(vals)


class HotelBillLine(models.Model):
    _name = 'hotel.bill.line'
    _description = 'Hotel Bill Line'

    bill_id = fields.Many2one(
        'hotel.bill',
        string='Bill',
        ondelete='cascade'
    )

    product_id = fields.Many2one(
        'product.product',
        string='Food Product',
        required=True
    )

    quantity = fields.Integer(
        string='Quantity',
        default=1
    )

    price = fields.Float(
        string='Price'
    )

    subtotal = fields.Float(
        string='Subtotal',
        compute='_compute_subtotal',
        store=True
    )

    @api.onchange('product_id')
    def onchange_product(self):
        if self.product_id:
            self.price = self.product_id.lst_price

    @api.depends('quantity', 'price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price