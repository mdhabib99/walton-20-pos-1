from odoo import models, fields, api, _  # noqa: F401


class Customers(models.Model):
    _name = "gbquotation.customers"
    _inherit = ["mail.thread"]
    _description = "GB Quotation Customers Model."

    company_name = fields.Char(string="Company Name", required=True)
    reg_address = fields.Char(string="Registared Address", required=True)
    contact_name = fields.Char(string="Contact Person Name", required=True)
    email = fields.Char(string="Email")
    mobile = fields.Char(string="Moblile Number", required=True)
    phone = fields.Char(string="Phone Number")
