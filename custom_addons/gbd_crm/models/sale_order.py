from odoo import models, fields, api


class GBSaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    _description = "Extra fields for Sale Order"

    loading_qty = fields.Integer(string="Load. Qty")
    container_qty = fields.Integer(string="Cont. Qty")
    container_type = fields.Many2one('gbd.container.type', string="Cont. Type")

    @api.onchange('loading_qty')
    def _onchange_loading_qty(self):
        if self.loading_qty and self.product_uom_qty:
            self.container_qty = self.product_uom_qty // self.loading_qty
