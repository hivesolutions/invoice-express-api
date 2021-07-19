#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import invoice_express

def get_api():
    return invoice_express.API(
        base_url = appier.conf("IE_BASE_URL"),
        key = appier.conf("IE_KEY")
    )
