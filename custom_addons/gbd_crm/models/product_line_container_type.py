from odoo import models, fields


class Container(models.Model):
    _name = "gbd.container.type"
    _description = "Container types for all sales order line"

    name = fields.Char(size=34, required=True, string="Type")
    description = fields.Char(size=60)
