# -*- coding: utf-8 -*-
{
    'name': "SlideShow",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Nien Pham Minh",
    'website': "https://www.w3schools.com/css/css_image_gallery.asp",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],
    
    # always loaded
    'data': [
        # 'security/picture.xml',
        'security/ir.model.access.csv',
        'views/snippets/nien_block.xml',
        'views/snippets/snippets.xml',
        'views/album.xml',
        # 'views/image.xml',
        
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'assets':{
        'web.assets_frontend': [
            'picture/static/src/scss/picture.scss',
            'picture/static/src/js/slideshow.js',
            
            
        ],
        'web._assets_primary_variables': [
        ],
        # 'web.asset_backend': [
        #     ''
        # ]
    },
    'images': [
    ],
    'snippet_lists': {
    },
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

