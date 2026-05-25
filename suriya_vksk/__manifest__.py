{
    'name': 'Hotel Billing',
    'version': '1.0',
    'summary': 'Hotel Food Billing and Monthly Sales Report',
    'author': 'VKSK Technologies',
    'category': 'Sales',
    'depends': ['base', 'product', 'mail'],
    'data': [
   	 'security/ir.model.access.csv',
   	 'data/sequence.xml',

   	 'report/hotel_bill_report.xml',

   	 'views/hotel_bill_views.xml',
   	 'views/report_views.xml',
   	 'views/menu.xml',

  	  'views/bill_report_template.xml',
],
    'installable': True,
    'application': True,
}
