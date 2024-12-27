from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    lpo_number = fields.Char(string="LPO Number")
    invoice_number = fields.Char(
        string="Invoice Number"
    )

  