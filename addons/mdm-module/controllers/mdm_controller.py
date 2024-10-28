from odoo import http
from odoo.http import request

class MDMController(http.Controller):

    @http.route('/mdm/device/register', type='json', auth='none', methods=['POST'])
    def register_device(self, serial_number, device_name, user_id):
        # Register the device in the Odoo system
        device = request.env['mdm.device'].sudo().create({
            'name': device_name,
            'serial_number': serial_number,
            'user_id': user_id,
        })
        return {'status': 'success', 'device_id': device.id}

    @http.route('/mdm/device/checkin', type='json', auth='none', methods=['POST'])
    def device_checkin(self, serial_number, battery_level, location):
        # Update device status during check-in
        device = request.env['mdm.device'].sudo().search([('serial_number', '=', serial_number)], limit=1)
        if device:
            device.write({'battery_level': battery_level, 'location': location, 'last_check_in': fields.Datetime.now()})
            return {'status': 'success'}
        return {'status': 'failed', 'error': 'Device not found'}

    @http.route('/mdm/device/get_policies', type='json', auth='none', methods=['POST'])
    def get_policies(self, serial_number):
        # Retrieve and send policies to the device
        device = request.env['mdm.device'].sudo().search([('serial_number', '=', serial_number)], limit=1)
        if device:
            policies = {
                'password_required': device.policy_password_required,
                'encryption_required': device.policy_encryption,
            }
            return {'status': 'success', 'policies': policies}
        return {'status': 'failed', 'error': 'Device not found'}
