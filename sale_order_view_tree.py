from odoo import api, fields, models
from datetime import datetime


class SaleOrderTree(models.Model):
    _name = "sale.order.tree.view"

    product_id = fields.Many2one('product.product', string="Product Name")
    default_code = fields.Char(string="Internal reference")
    order_qty = fields.Float(string="Ordered Quantity")
    over_all_sale = fields.Float(string="Sub total")
    unit_prz = fields.Float(string="Unit Price")

    @api.multi
    def sale_order_tree_view(self):
        # res_line = self.env['sale.order.line'].search([])
        rec_product = self.env['product.product'].search([])
        for i in rec_product:
            sol = self.env['sale.order.line'].search([('product_id', '=', i.id)])
            qty = 0
            subtotal = 0
            prz_unit = 0
            for j in sol:
                qty += j.product_uom_qty
                subtotal += j.price_subtotal
                prz_unit += j.price_unit
            self.create({'product_id': i.id,
                         'default_code': i.default_code,
                         'order_qty': qty,
                         'over_all_sale': subtotal,
                         'unit_prz': prz_unit,
                         })



