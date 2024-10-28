from odoo import models, fields


class HsCode(models.Model):
    _name = "gbd.hs.code"
    _description = "Custom GBD HS Code Table"

    name = fields.Char(string="HS Code", required=True)
    description = fields.Text()
