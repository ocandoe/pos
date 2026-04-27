/** @odoo-module */
// This line tells Odoo that this is an Odoo module

import { ReceiptScreen } from "@point_of_sale/app/screens/receipt_screen/receipt_screen";
import { patch } from "@web/core/utils/patch";

patch(ReceiptScreen.prototype, {
    setup() {
        super.setup(...arguments)
        self = this
        this.env.services.orm.call('pos.order','get_invoice',[self.currentOrder.pos_reference]).then(function(invoice){
            self.currentOrder.set_invoice(invoice)
        })
    },
});
