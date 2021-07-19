#!/usr/bin/python
# -*- coding: utf-8 -*-

class InvoiceAPI(object):

    def list_invoices(self, *args, **kwargs):
        url = self.base_url + "invoices.json"
        contents = self.get(url, **kwargs)
        return contents

    def create_invoice(self, invoice):
        url = self.base_url + "invoices.json"
        contents = self.post(url, data_j = dict(invoice = invoice))
        return contents

    def get_invoice(self, id):
        url = self.base_url + "invoices/%s.json" % id
        contents = self.get(url)
        return contents

    def finalize_invoice(self, id, message = "Finalized"):
        url = self.base_url + "invoices/%s/change-state.json" % id
        contents = self.post(
            url,
            data_j = dict(
                invoice = dict(
                    state = "finalized",
                    message = message
                )
            )
        )
        return contents

    def pdf_invoice(self, id):
        url = self.base_url + "api/pdf/%s.json" % id
        contents = self.get(url)
        return contents
