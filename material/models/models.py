# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class material(models.Model):
    _name = 'material.material'
    _description = 'Material'

    code = fields.Char("Material Code", required=1)
    name = fields.Char("Material Name", required=1)
    buy_price = fields.Float("Material Buy Price", required=1)
    supplier_id = fields.Many2one(string='Related supplier', comodel_name='res.partner', required=1)
    material_type = fields.Selection(
        string='Material Type',
        required=1,
        selection=[('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')]
    )
        
    @api.model
    def create(self, vals):
        res = super(material, self).create(vals)
        if res and not res.buy_price or (res.buy_price and res.buy_price < 100):
            raise UserError("Material buy price tidak boleh dibawah 100")
        return res
    
    def write(self,vals):
        res = super(material, self).write(vals)
        if res and not self.buy_price or (self.buy_price and self.buy_price < 100):
            raise UserError("Material buy price tidak boleh dibawah 100")
        return res
    
    @api.onchange('buy_price')
    def _onchange_buy_price(self):
        if self.buy_price and self.buy_price < 100:
            raise UserError("Material buy price tidak boleh dibawah 100")
        
    def get_data(self):
        json_data_material = []
        material_list = self.search([])
        for data_material in material_list:
            supplier = self.env['res.partner'].browse(data_material.supplier_id.id).name
            json_data_material.append({
                'code': data_material.code,
                'name': data_material.name,
                'material_type': data_material.material_type,
                'buy_price': data_material.buy_price,
                'supplier_id': supplier
            })
        
        return json_data_material
