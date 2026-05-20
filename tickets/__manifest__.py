{
    'name':'Ticket',
    'version':'1.0',
    'author':'Suriya technologies',
    'description':'Ticket tool for Apdeops',
    'categery':'Tools',
    'depends':['base','mail'],
    'data':[
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/tickets.xml',

    ],

    'installable':True,
    'application':True,
}
