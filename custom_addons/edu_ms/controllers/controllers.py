
from odoo import http


class Edu_ms(http.Controller):
    @http.route('/edu_ms/edu_ms', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/edu_ms/edu_ms/objects', auth='public')
    def list(self, **kw):
        return http.request.render('edu_ms.listing', {
            'root': '/edu_ms/edu_ms',
            'objects': http.request.env['edu.student'].search([]),
        })

    @http.route('/edu_ms/edu_ms/objects/<model("edu_ms.edu_ms"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('edu_ms.object', {
            'object': obj
        })