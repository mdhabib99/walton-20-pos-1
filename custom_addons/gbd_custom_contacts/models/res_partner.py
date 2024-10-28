"""
File: res_partner.py
Author: K. M. Jiaul Islam Jibon
Date: 2023-09-20

Description:
This module is responsible for override the existing fields and customization
of the contact form.

"""

from odoo import api, fields, models

# Define a list of reference type items as a tuple of key-value pairs
REFERENCE_TYPE_OPTIONS = [
    ("internal", "Internal"),
    ("external", "External"),
    ("self", "Self"),
]

# Currency accepted LOV
CURRENCY_LOV = [("usd", "USD"), ("inr", "INR"), ("euro", "EURO"), ("rmb", "RMB")]

# Textual Booleans
BOOLEAN_TXT_LOV = [("allowed", "Allowed"), ("not_allowed", "Not Allowed")]

BOOLEAN_YN_LOV = [("yes", "Yes"), ("no", "No")]

SERVICE_CHARGE_CATEGORY_LOV = [("buyer", "Buyer"), ("supplier", "Supplier")]


class Agreements(models.Model):
    """Custom GBD table for holding the agreements. A single contact may have 1 or more agreements"""

    _name = "gbd.contact.agreement"
    _description = "GBD Contact Agreement section data"

    partner_id = fields.Many2one(
        "res.partner", string="Partner"
    )  # Many2one field to link to ResPartner
    attachment = fields.Binary(string="Attachment", attachment=True)
    attachment_name = fields.Char(string="Attachment Name")
    effective_from = fields.Date(string="Effective from (Start Date)", required=True)
    effective_to = fields.Date(string="Valid till (End Date)", required=True)
    agreement_remarks = fields.Text(string="Agreement Remarks")


class ResPartner(models.Model):
    """
    Customization of the res.partner model to add additional fields and functionality.
    """

    # Inherit the res.partner model
    _inherit = "res.partner"

    # Change the existing type options. Removed the other Address and merged with Contact
    type = fields.Selection(
        selection="_get_new_address_types",
        string="Address Type",
        default="contact",
        help="- Contact: Use this to organize the contact details of employees of a given company (e.g. CEO, CFO, ...).\n"
             "- Invoice Address : Preferred address for all invoices. Selected by default when you invoice an order that belongs to this company.\n"
             "- Delivery Address : Preferred address for all deliveries. Selected by default when you deliver an order that belongs to this company.\n"
             "- Private: Private addresses are only visible by authorized users and contain sensitive data (employee home addresses, ...).\n",
    )

    # Inherit and Change the String for existing fields
    phone = fields.Char(unaccent=False, string="Customer Phone")
    mobile = fields.Char(unaccent=False, string="Customer Mobile")

    # Define custom fields
    region = fields.Char(string="Region")
    zone = fields.Char(string="Zone")
    customer_id = fields.Char(string="Customer ID", readonly=True)
    ebs_id = fields.Char(string="EBS ID", readonly=True)
    sales_channel = fields.Char(string="Sale Channel")
    brand_name = fields.Char(string="Brand Name")
    business_type = fields.Many2one("gbd.business.type.lov", string="Business Type")
    product_category = fields.Many2many(
        "product.category", string="Product Category", ondelete="restrict"
    )
    business_region = fields.Char(string="Business Region")
    reference_source = fields.Selection(
        selection=REFERENCE_TYPE_OPTIONS, string="Source Reference", default="internal"
    )
    remarks = fields.Text(string="Remarks")
    # Agreements O2M
    gbd_contact_agreement_ids = fields.One2many(
        "gbd.contact.agreement", "partner_id", string="Agreements"
    )
    # delivery team
    inco_term = fields.Many2many(
        "gbd.incoterm.lov", string="IncoTerm", ondelete="restrict"
    )
    loading_port = fields.Many2many(
        "gbd.landing.port.lov", string="Port of Loading", ondelete="restrict"
    )
    discharge_port = fields.Many2many(
        "gbd.discharge.port.lov", string="Discharge Port", ondelete="restrict"
    )
    shipment_mode = fields.Many2many(
        "gbd.shipment.mode.lov", string="Shipment Mode", ondelete="restrict"
    )
    tran_partial_shipment = fields.Selection(
        BOOLEAN_TXT_LOV, string="Trans & Partial Shipment"
    )
    # payment fields
    payment_type = fields.Many2many(
        "gbd.payment.type.lov", string="Payment Type", ondelete="restrict"
    )
    payment_term = fields.Many2one("gbd.payment.term.lov", string="Payment Terms")
    currency_type = fields.Selection(selection=CURRENCY_LOV, string="Payment Currency")
    # Marketing & Branding
    budget = fields.Char(string="Budget")
    artworks = fields.Char(string="Artworks")
    marketing_activities_implementation = fields.Char(
        string="Marketing Activities Implementation"
    )
    marketing_activities_approval = fields.Char(string="Marketing Activities Approval")
    tolerance = fields.Char(string="Tolerance")
    # After Sales Service
    toll_free_phone = fields.Char(string="Toll Free Phone Number")
    coordinator = fields.Char(string="Coordinator")
    thirdparty_vendor = fields.Char(string="3rd Party Vendor")
    service_platform = fields.Char(string="Walton's Service Platform")
    spare_parts = fields.Char(string="FOC Spare Parts(%)")
    #  Warranty
    doa = fields.Selection(BOOLEAN_YN_LOV, string="Product Warranty /DOA")
    major_parts = fields.Selection(BOOLEAN_YN_LOV, string="Major Parts")
    minor_parts = fields.Selection(BOOLEAN_YN_LOV, string="Minor Parts")
    service_charge = fields.Selection(
        SERVICE_CHARGE_CATEGORY_LOV, string="Service Charge"
    )
    transportation_cost = fields.Selection(
        SERVICE_CHARGE_CATEGORY_LOV, string="Transportation Cost"
    )
    # Certifications
    import_certification = fields.Char(string="Import Certification")
    export_certification = fields.Char(string="Export Certification")
    product_certification = fields.Char(string="Product Certification")
    factory_certification = fields.Char(string="Factory Certification")
    component_certification = fields.Char(string="Component Certification")
    liability_insurance = fields.Char(string="Product liability Insurance")
    power_plug_type = fields.Char(string="Power Plug Type")

    @api.model
    def _get_new_address_types(self):
        selection = [
            ("contact", "Contact"),
            ("invoice", "Invoice Address"),
            ("delivery", "Delivery Address"),
            ("private", "Private Address"),
        ]
        return selection

    @api.onchange("country_id")
    def _onchange_country_id(self):
        """
        Override the onchange method for the country_id field.
        This method sets the ISD code for the selected country in the customer_phone field.
        """
        # Handle the default task from the super class
        super()._onchange_country_id()

        # Set the ISD code for the selected country if it has a phone code
        phone_code = self.country_id.phone_code

        if phone_code:
            self.phone = f"+{phone_code}"
            self.mobile = f"+{phone_code}"

    @api.model
    def create(self, vals):
        vals["customer_id"] = self.env["ir.sequence"].next_by_code(
            "gbd.contact.customerid"
        )
        vals["ebs_id"] = self.env["ir.sequence"].next_by_code(
            "gbd.contact.ebsid"
        )  # for demo purpose only. In future will handle through API
        return super(ResPartner, self).create(vals)
