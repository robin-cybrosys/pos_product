  odoo.define('pos_product.grade', function(require){
    'use strict';
    var models = require('point_of_sale.models');
    var _super_product = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({
        initialize: function(session, attributes){
            var self = this;
            models.load_fields('product.product', ['grade','rating']);
            _super_product.initialize.apply(this, arguments);
        }
    });
});
//Now we can pass this field to the receipt.
odoo.define('module_name.receipt', function(require){
    "use strict";
    console.log('start');
    var models = require('point_of_sale.models');
    models.load_fields('product.product', ['grade','rating']);
    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        export_for_printing: function(){
            var line = _super_orderline.export_for_printing.apply(this, arguments);
            line.grade = this.get_product().grade;
            line.rating = this.get_product().rating;
//            console.log(line.grade);
//            console.log(line.rating,"ratinggg");
            return line;
        }
    });
});
