# -*- coding: utf-8 -*-
# from odoo import http


# class L10nGtCrsPos(http.Controller):
#     @http.route('/l10n_gt_crs_pos/l10n_gt_crs_pos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_gt_crs_pos/l10n_gt_crs_pos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_gt_crs_pos.listing', {
#             'root': '/l10n_gt_crs_pos/l10n_gt_crs_pos',
#             'objects': http.request.env['l10n_gt_crs_pos.l10n_gt_crs_pos'].search([]),
#         })

#     @http.route('/l10n_gt_crs_pos/l10n_gt_crs_pos/objects/<model("l10n_gt_crs_pos.l10n_gt_crs_pos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_gt_crs_pos.object', {
#             'object': obj
#         })
