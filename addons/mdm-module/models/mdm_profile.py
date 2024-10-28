from odoo import models, fields

class MdmProfile(models.Model):
    _name = 'mdm.profile'
    _description = 'MDM Profile'

    name = fields.Char(string='Profile Name', required=True)
