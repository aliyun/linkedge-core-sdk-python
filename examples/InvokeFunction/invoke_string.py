# -*- coding: utf-8 -*-
import logging  
import lecoresdk
import time
import json
import base64


def handler(event, context):
  fc = lecoresdk.Client()
  context = {"custom": {"data": "customData"}}

  context_str = json.dumps(context)
  context_bytes = base64.standard_b64encode(context_str.encode("utf-8"))
  invokerContext = context_bytes.decode("utf-8")
  invokeParams = {
    "serviceName": 'Invokee service Name',
    "functionName": 'Invokee Function Name',
    "invocationType": 'Sync',
    "invokerContext": invokerContext,
    "payload": 'String message from Invoker.'
  };
  fc.invoke_function(invokeParams)

  return 'hello world'
