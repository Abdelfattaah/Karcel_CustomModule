{
    'name': 'Karcel Task',
    'author': 'Abdelfattah Mohamed',

    'depends': [
        'base',
        'website',
        'sale_management',
    ],

    'data': [
        'views/car_search_view.xml',
        'security/ir.model.access.csv',
    ],

    'post_init_hook': 'sample_data',

    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
            'karcel_task/static/src/css/*.css',
            'karcel_task/static/src/js/main.js',
        ],
        'web.assets_common': [
        ],
    },
    'license': 'AGPL-3',
}
