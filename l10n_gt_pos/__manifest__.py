# -*- coding: utf-8 -*-
{
    'name': "Guatemala - Punto de Venta",
    'summary': """Módulo que amplía las funcionalidades del punto de venta para que sea compatible con la factura electrónica de guatemala""",
    'author': "CORSISA",
    'website': "http://www.corsisa.com.gt",
    'category': 'Customizations',
    'version': '19.0.1.0.1',
    'license': 'LGPL-3',
    'countries': ['gt'],

    'depends': ['point_of_sale','l10n_gt_crs'],

    'data': [
        #"security/ir.model.access.csv",
        "views/res_config_settings.xml",
        #'report/pos_order_ticket.xml',
        #'report/report.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'l10n_gt_pos/static/src/**/*',
        ],    

    }
}
