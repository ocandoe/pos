from odoo import _, models, fields
import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import UserError, ValidationError
class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_partner(self):
        res = super(PosSession, self)._loader_params_res_partner()
        res['search_params']['fields'].append('cui')
        return res

    def action_pos_session_close(self, balancing_account=False, amount_to_balance=0, bank_payment_method_diffs=None):

        close_session = self.env['res.company'].search([('id', '=', self.env.company.id)]).close_session_restrition
        if not close_session:

            orders = self.order_ids.filtered(lambda order: order.state != 'invoiced' and order.amount_total > 0)
            if len(orders) > 0:
                raise ValidationError(
                    'Tiene pedidos sin factura, no puede cerrar sesión mientras no haya facturado todos los pedidos.')

        res = super(PosSession, self).action_pos_session_close(balancing_account, amount_to_balance, bank_payment_method_diffs)
        return res
