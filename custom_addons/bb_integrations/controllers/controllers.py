from odoo import http

from ..utils import authKeyRequired, logTracer

V1_API = "/api/v1"

ROUTE_PREFIX = V1_API + "/services/orcl"

KEY_IDENTIFIER = "API_KEY"
API_KEY = "ORCLTESTME@123"


class SyncInventoryController(http.Controller):
    def _update_product_quantity(self, product, location, qty):
        quant = (
            http.request.env["stock.quant"]
            .sudo()
            .search([("product_id", "=", product.id), ("location_id", "=", location.id)], limit=1)
        )

        if quant:
            quant.quantity = qty
        else:
            http.request.env["stock.quant"].sudo().create(
                {"product_id": product.id, "location_id": location.id, "quantity": qty}
            )

    def _convert_qty_to_sell_uom(self, product, qty):
        factor = product.product_tmpl_id.uom_id.factor
        quant = factor * float(qty)
        return quant

    @http.route(f"{ROUTE_PREFIX}/sync-inventory", auth="public", methods=["POST"], type="json", website=False)
    @logTracer
    @authKeyRequired
    def index(self, **kw):
        kw.pop("API_KEY")
        product = kw["InputParameters"]["P_INPITMTRANTABTYP"]["P_INPITMTRANTABTYP_ITEM"]
        item_code = product.get("ITEM_CODE")
        qty = product.get("TRANSACTION_QUATITY")
        store = product.get("SUBINVENTORY")

        if not all([item_code, qty, store]):
            return {"status": "error", "message": "Missing requried fields !"}
        product = http.request.env["product.product"].sudo().search([("default_code", "=", item_code)], limit=1)
        
        if not product:
            return {"status": "error", "message": "Product not found !"}
        
        location = http.request.env['stock.location'].sudo().search([("name", "=", store)], limit=1)

        if not location:
            return {
                'status': 'error',
                'message': 'Location not found!'
            }
        
        qty = self._convert_qty_to_sell_uom(product, qty)

        self._update_product_quantity(product, location, float(qty))

        return {"status": "success", "message": "product quantity has been updated."}
