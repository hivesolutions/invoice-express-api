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
