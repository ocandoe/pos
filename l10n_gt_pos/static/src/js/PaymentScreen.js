/** @odoo-module */
// This line tells Odoo that this is an Odoo module

import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";

patch(PaymentScreen.prototype, {
  setup() {

    super.setup()

    const checkInvoiceAutoCheck = async () => {
      const result = await  this.env.services.orm.call(
          'res.config.settings',
          'get_values',
          [],
      );
      const invoiceAutoCheck = result.invoice_auto_check;
      return invoiceAutoCheck;
  };
  checkInvoiceAutoCheck().then((isAutoCheckEnabled) => {
    if (isAutoCheckEnabled) {
        this.currentOrder.set_to_invoice(true);
    }
});

  },
});
