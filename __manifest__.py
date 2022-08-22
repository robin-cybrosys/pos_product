{
    'name': "Pos Product Grade",

    'application': "True",

    'sequence': "-11",

    'author': "Cybrosys Technologies",

    'website': "http://www.cybrosys.com",

    'version': '15.0.1.0.0',

    'licence': "LGPL-3",

    'depends': ['base', 'sale', 'point_of_sale'],
    'assets': {
        'web.assets_qweb': [
            "pos_product/static/src/xml/pos_product_grade.xml"],
        'web.assets_backend': [
            "pos_product/static/src/js/grade.js"]
    },

    'data': [
        'views/product.xml',
    ],
}
