
from odoo import models, fields, api

class MDMDevice(models.Model):
    _name = 'mdm.device'  # Model name used in the database
    _description = 'MDM Android Device'

    name = fields.Char(string='Device Name', required=True)  # Name of the Android device
    serial_number = fields.Char(string='Serial Number', required=True, unique=True)  # Unique ID of the device
    user_id = fields.Many2one('res.users', string='Assigned User')  # Reference to the user assigned to this device
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive'), ('locked', 'Locked')],
                              string='Status', default='active')  # Device status (e.g., active, locked)
    last_check_in = fields.Datetime(string='Last Check-In')  # Last time the device checked in with Odoo
    battery_level = fields.Float(string='Battery Level')  # Battery status reported by the device
    location = fields.Char(string='Location')  # Location of the device reported during check-in
    # Policy fields for the device
    policy_password_required = fields.Boolean(string='Password Required', default=True)  # Enforce password policy
    policy_encryption = fields.Boolean(string='Encryption Required', default=False)  # Enforce encryption policy
