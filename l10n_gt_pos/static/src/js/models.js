/** @odoo-module */

import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";
import { uuidv4, qrCodeSrc } from "@point_of_sale/utils";
patch(PosOrder.prototype, {

    setup() {
        super.setup(...arguments);

    },
    export_for_printing() {
        var receipt = super.export_for_printing(...arguments);
        if (this.invoice) {
            receipt.invoice = this.invoice;
            receipt.client = this.get_partner()
            receipt.pos_qr_code = qrCodeSrc(`${this.invoice.qr_image}`)
        }
        return receipt
    },
    set_invoice(receipt) {
        this.invoice =receipt

    }


});