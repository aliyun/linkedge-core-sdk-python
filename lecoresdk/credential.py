#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import logging
from runtime_utils import config
from runtime_utils import ipc_wrapper


class CredentialProviderChain(object):
    _instance = None

    def __new__(self, *args, **kw):
        if not self._instance:
            self._instance = super(CredentialProviderChain, self).__new__(self)
            self._instance.providers = []
            self._instance.providers.append(DefaultCredentialProvider())
        return self._instance

    def get_credential(self):
        return self.providers[0].get()


class DefaultCredentialProvider(object):
    def __init__(self):
        self.ipc = ipc_wrapper.ipc
        self.uri = os.environ.get('DEFFAULT_CREDENTIALS_RELATIVE_URI')

    def get(self):
        cred_msg = self.ipc.get_credential(self.uri)
        if cred_msg is not None and "statusCode" in cred_msg["msg"]:
            statusCode = cred_msg["msg"]["statusCode"]
            if statusCode == 200:
                if "headers" in cred_msg["msg"]:
                    headers = cred_msg["msg"]["headers"]
                    cred = headers[config.HEADER_PROV_CREDENTIAL]
                    try:
                        cred_json = json.loads(cred)
                        return cred_json
                    except Exception:
                        logging.error("cant gen json format.")
                else:
                    logging.error("header not in cred_msg.")
            else:
                logging.error("FC_PYTHON:get credential fail: %s", statusCode)
        else:
            logging.error("cred_msg get timeout.")
