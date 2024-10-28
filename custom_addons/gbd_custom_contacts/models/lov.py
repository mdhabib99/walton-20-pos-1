from odoo import models, fields


class ShipmentModeLov(models.Model):
    _name = "gbd.shipment.mode.lov"
    _description = "GBD Shipment Mode"

    name = fields.Char(string="Shipment Mode", required=True)

    def __str__(self) -> str:
        return self.name


class LandingPortLov(models.Model):
    _name = "gbd.landing.port.lov"
    _description = "GBD all the Landing Port"

    name = fields.Char(string="Landing Port", required=True)

    def __str__(self) -> str:
        return self.name


class DischargePortLov(models.Model):
    _name = "gbd.discharge.port.lov"
    _description = "GBD all the Discharge Port"

    name = fields.Char(string="Discharge Port", required=True)

    def __str__(self) -> str:
        return self.name


class IncoTermLov(models.Model):
    _name = "gbd.incoterm.lov"
    _description = "GBD IncoTerms"

    name = fields.Char(string="Incoterm", required=True)

    def __str__(self) -> str:
        return self.name


class PaymentType(models.Model):
    _name = "gbd.payment.type.lov"
    _description = "GBD Accepted Payment Types"

    name = fields.Char(string="Payment Type", required=True)

    def __str__(self) -> str:
        return self.name


class PaymentTerm(models.Model):
    _name = "gbd.payment.term.lov"
    _description = "GBD Accepted Payment Terms"

    name = fields.Char(string="Payment Type", required=True)

    def __str__(self) -> str:
        return self.name


class BusinessType(models.Model):
    _name = "gbd.business.type.lov"
    _description = "Business Types for GBD Sales & Purchase"

    name = fields.Char(size=80, string="Business Type")

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Choose another value - it has to be unique!')
    ]

    def __str__(self) -> str:
        return self.name
