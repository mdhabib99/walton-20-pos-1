from odoo import models, fields


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    swift_code = fields.Char(string="Swift Code")
    address = fields.Text(string="Address")
    contact = fields.Char(string="Contact")
    email_id = fields.Char(string="Email")
    allow_out_payment = fields.Boolean(compute='_compute_allow_out_payment', store=False)
    comments = fields.Char(size=100)

    def _compute_allow_out_payment(self):
        for record in self:
            record.allow_out_payment = None
