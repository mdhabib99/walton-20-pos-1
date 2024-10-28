from odoo import models, fields, api, _  # noqa: F401


class GbQuotation(models.Model):
    _name = "gbquotation.quotation"
    _inherit = ["mail.thread"]
    _description = "GB Quotation Model."
