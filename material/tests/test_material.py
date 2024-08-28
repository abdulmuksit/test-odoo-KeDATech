from odoo.tests.common import TransactionCase

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.partner_obj = self.env['res.partner']
        self.material_obj = self.env['material.material']

    def test_create_material(self):
        partner_id = self.test_create_partner()

        # Create data material
        material = self.material_obj.create({
            'code':'Jeans1',
            'name':'Bahan Jeans 1M',
            'buy_price': 100,
            'material_type': 'jeans',
            'supplier_id':partner_id.id
        })
        print(material.name)

        # Write data material
        material.write({
            'name':'Bahan Jeans 2M'
        })
        print(material.name)

        # Delete data material
        material.unlink()

        # Search all data material
        all_data_material = self.material_obj.search([])
        for data_material in all_data_material:
            print(data_material.name)

    def test_create_partner(self):
        partner = self.partner_obj.create({
            'name': 'Alexa',
            'email': 'alexa@gmail.com'
        })
        
        return partner
