/** @odoo-module **/

//export const session = odoo.__session_info__ || {};
export let session = odoo.__session_info__ || {};
session.support_url = "https://waltondigitech.com/contact-us"
//export session;
delete odoo.__session_info__;
