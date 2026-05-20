from odoo import models, fields, api


class Tickets(models.Model):
    _name = 'tickets'
    _description = "Tickets"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Ticket Id",
        required=True,
        copy=False,
        readonly=True,
        default="New"
    )

    subject = fields.Char(string="Subject", required=True, tracking=True)
    description = fields.Text(string="Description")

    employee_id = fields.Many2one(
        'res.users',
        string="Requested by",
        tracking=True,
        default=lambda self: self.env.user
    )

    assigned_to = fields.Many2one(
        'res.users',
        string="Assigned To",
        tracking=True
    )

    priority = fields.Selection(
        [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High')
        ],
        default="medium",
        tracking=True,
    )

    department = fields.Selection(
        [
            ('infra', 'Infra'),
            ('devops', 'DevOps'),
            ('hr', 'HR'),
            ('db', 'DB'),
            ('rim', 'RIM')
        ],
        string="Department",
        tracking=True,
    )

    state = fields.Selection(
        [
            ('new', 'NEW'),
            ('inprogress', 'IN PROGRESS'),
            ('hold', 'Hold'),
            ('closed', 'Closed')
        ],
        default="new",
        tracking=True,
    )

    created_date = fields.Datetime(string="Created Date", readonly=True)
    closed_date = fields.Datetime(string="Closed Date", readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == "New":
            vals['name'] = self.env['ir.sequence'].next_by_code('tickets') or 'New'
        return super(Tickets, self).create(vals)

    def action_start(self):
        self.state = 'inprogress'

    def action_closed(self):
        self.state = 'closed'
        self.closed_date = fields.Datetime.now()

    def action_hold(self):
        self.state = "hold"

    def action_reset(self):
        self.state = "new"
