#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class InvoiceExpressApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "invoice_express",
            *args, **kwargs
        )

    @appier.route("/", "GET")
    def index(self):
        return self.invoices()

    @appier.route("/invoices", "GET")
    def invoices(self):
        api = self.get_api()
        invoices = api.list_invoices()
        return invoices

    @appier.route("/invoices/create", "GET")
    def create_invoice(self):
        finalize = self.field("finalize", True, cast = bool)
        pdf = self.field("pdf", False, cast = bool)
        api = self.get_api()
        invoice = api.create_invoice(
            dict(
                date = "01/01/2023",
                due_date = "01/02/2023",
                client = dict(name = "DUMMY", code = "DUM"),
                items = [
                    dict(
                        name = "BAR",
                        description = "Chocolate Bar",
                        unit_price = "123,0000",
                        quantity = "1"
                    )
                ]
            )
        )
        invoice_id = invoice["invoice"]["id"]
        if finalize: api.finalize_invoice(invoice_id)
        invoice = api.get_invoice(invoice_id)
        if pdf:
            pdf_invoice = api.pdf_invoice(invoice_id)
            return self.redirect(pdf_invoice["output"]["pdfUrl"])
        return invoice

    @appier.route("/invoices/<str:id>", "GET")
    def invoice(self, id):
        api = self.get_api()
        invoice = api.get_invoice(id)
        return invoice

    def get_api(self):
        return base.get_api()

if __name__ == "__main__":
    app = InvoiceExpressApp()
    app.serve()
else:
    __path__ = []
