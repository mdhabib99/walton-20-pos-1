from odoo import models, fields

class MdmApp(models.Model):
    _name = 'mdm.app'
    _description = 'MDM App'

    name = fields.Char(string='App Name', required=True)
    version = fields.Char(string='Version')
