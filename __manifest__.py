{
    'name': 'Custom Delivery Slip',
    'version': '1.0',
    'summary': 'Add LPO and Invoice Number to Delivery Slip',
    'author': 'James Otieno',
    'depends': ['stock', 'account', 'sale', 'sale_stock'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
}
