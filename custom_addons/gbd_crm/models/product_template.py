from odoo import models, fields, api


class GBDProduct(models.Model):
    _inherit = "product.template"
    _description = "Customization for products for GBD"

    item_code: str = fields.Char(size=28)
    hscode_id: int = fields.Many2one('gbd.hs.code', string="HS Code")

    @api.onchange('item_code')
    def _onchange_item_code(self) -> None:
        if self.item_code:
            self.item_code = self.item_code.upper()
