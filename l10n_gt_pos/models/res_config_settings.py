# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    close_session = fields.Boolean(related='company_id.close_session_restrition', readonly=False)
    qr_ticket = fields.Boolean(related='company_id.qr_ticket', readonly=False)
    invoice_auto_check = fields.Boolean()

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('res.config.settings.invoice_auto_check',
                  int(self.invoice_auto_check))

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res['invoice_auto_check'] = int(
            get_param('res.config.settings.invoice_auto_check'))
        return res