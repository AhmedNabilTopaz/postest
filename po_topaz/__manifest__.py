# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'PO Fabric Topaz',
    'version': '1.0',
    'summary': 'Editing PO Style ',
    'description': "",
    'website': 'https://www.odoo.com/app/inventory',
    'depends': ['account', 'purchase', 'sale', 'stock'],
    'sequence': -100,
    'data': [
        'report/po_template.xml'
    ],
    'license': 'LGPL-3'

}
