# mdm_module/controllers/mdm_api.py
from odoo import http
from odoo.http import request
import json

class MDMApiController(http.Controller):

    @http.route('/mdm/enroll', type='json', auth='public', methods=['POST'])

    def enroll_device(self, **post):
        device_id = post.get('device_id')
        device_name = post.get('device_name')
        # Add logic to register device in Odoo
        device = http.request.env['mdm.device'].sudo().create({
            'name': device_name,
            'device_id': device_id,
        })
        return json.dumps({'status': 'success', 'device_id': device.id})

    @http.route('/mdm/push_policy', type='json', auth='public', methods=['POST'])
    def push_policy(self, **post):
        device_id = post.get('device_id')
        policy_data = post.get('policy')
        # Implement logic to push policies to the device
        return json.dumps({'status': 'policy_sent'})
