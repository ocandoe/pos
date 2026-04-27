from odoo import models, api

import logging

_logger = logging.getLogger(__name__)


class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def get_invoice(self, id):
        pos_id = self.search([('pos_reference', '=', id)], limit=1)
        invoice_id = self.env['account.move'].search([('id', '=', pos_id.account_move.id)], limit=1)
        company_id = self.env['res.company'].search([('id', '=', pos_id.company_id.id)], limit=1)
        branch_id = company_id.parent_id
        journal_id = invoice_id.journal_id
        account_move = invoice_id.company_id.parent_id if invoice_id.company_id.parent_id else invoice_id.company_id
        isr_phrase = account_move.get_scenary_isr_label(account_move.scenary_isr)
        iva_phrase = account_move.get_scenary_iva_label(account_move.scenary_iva)
        vat = branch_id.vat if branch_id.vat else company_id.vat
        qr_image = invoice_id.qr_string if self.env.company.qr_ticket else False
        return {
            'invoice_id': invoice_id.id,
            'invoice_name': invoice_id.name,
            'move_type': invoice_id.move_type,
            'fel_number': invoice_id.fel_number,
            'fel_serie': invoice_id.fel_serie,
            'fel_uuid': invoice_id.fel_uuid,
            'fel_certification_date': invoice_id.fel_certification_date,
            'commercial_partner_id_name': invoice_id.commercial_partner_id.name,
            'commercial_partner_id_street': invoice_id.commercial_partner_id.street,
            'commercial_partner_id_vat': invoice_id.commercial_partner_id.vat,
            'commercial_partner_id_cui': invoice_id.commercial_partner_id.cui,
            'commercial_name': company_id.establishment_name if company_id.establishment_name else branch_id.establishment_name,
            'commercial_address': company_id.street if company_id.street else branch_id.street,
            'company_name': branch_id.name if branch_id.name else company_id.name,
            'commercial_phone': company_id.phone if company_id.phone else branch_id.phone,
            'cert_name': branch_id.certifier_name if branch_id.certifier_name else company_id.certifier_name,
            'cert_vat': branch_id.certifier_vat if branch_id.certifier_vat else company_id.certifier_vat,
            'fel_dte_type': journal_id.fel_dte_type,
            'reversed_fel_number': invoice_id.reversed_entry_id.fel_number,
            'reversed_fel_serie': invoice_id.reversed_entry_id.fel_serie,
            'reversed_fel_uuid': invoice_id.reversed_entry_id.fel_uuid,
            'reversed_fel_date': invoice_id.reversed_entry_id.invoice_date,
            'scenary_isr': isr_phrase,
            'scenary_iva': iva_phrase,
            'vat': vat,
            'qr_image': qr_image,
        }

