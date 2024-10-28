from odoo import models, fields
class MdmPolicy(models.Model):
    _name = 'mdm.policy'
    _description = 'MDM Policy'

    name =fields.Char(string='policy Name', required=True)
    description = fields.Text(string='Description')