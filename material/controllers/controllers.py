# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Material(http.Controller):
    @http.route('/material/api', auth='public', website=False, csrf=False, type='json', methods=['GET', 'POST'])
    def index(self, **kw):
        material_list = request.env['material.material'].get_data()
        return material_list
