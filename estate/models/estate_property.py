from odoo import fields, models
from datetime import timedelta

class EstateProperty(models.Model):
    active = fields.Boolean('Active', default = True)
    _name = "estate.property"
    _description = "Estate Property"
    name = fields.Char('Property Name', required=True, translate=True)
    description = fields.Text('Description')
    postcode = fields.Char('Zip Code', required=True, translate=True)
    date_availability = fields.Date('Date Available', default=lambda self: fields.Datetime.now() + timedelta(days = 90))
    expected_price = fields.Float('Expected Price')
    selling_price = fields.Float('Selling Price', readonly = True)
    bedrooms = fields.Integer('Bedrooms', default = 2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Good example of help text to explain fields")
    state = fields.Selection(string = 'State', selection = [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), 
        ('sold', 'Sold'), ('cancelled', 'Cancelled')])

