{
    'name':'Suriya Manfacturing',
    'version':'1.0',
    'description':'The Module for Manafacuring flow',
    'author':'Suriya Technologies',
    'category':'Manafacturing',
    'depends':['base','sale_management','crm','stock'],
    'data':[
        'security/ir.model.access.csv',
        'views/steel_order.xml',
        'views/sales_views.xml',
        'views/crm_views.xml',
    ],

    'installable':True,
    'application':True,
}