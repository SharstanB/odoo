from odoo import fields, models


class Property(models.Model):
    _name = "property.properties"
    _description = "this module for property basic details"
    _order = "sequence"

    name = fields.Char('Plan Name', required=True, translate=True)
    number_of_months = fields.Integer('# Months', required=True)
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)

    _sql_constraints = [
        ('check_number_of_months', 'CHECK(number_of_months >= 0)', 'The number of month can\'t be negative.'),
    ]