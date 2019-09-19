#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import json
import base64
from runtime_utils import config
from runtime_utils import sync
from runtime_utils import fc_error
from runtime_utils import utils
from runtime_utils import ipc_wrapper


# {functionName: "functionid", invocaionType: "Sync or Async.", payload: ""}
class Client(object):
    def __init__(self):
        self.ipc = ipc_wrapper.ipc
        self.invokeSync = sync.SyncMsg_Event()

    def _getInvokeResult_cb(self, status, data):
        syncMsg = {}
        syncMsg["state"] = False
        syncMsg["msg"] = None
        try:
            if status == "success":
                logging.debug("staus:%s", status)
                syncMsg["state"] = True
                syncMsg["msg"] = data
            else:
                syncMsg["msg"] = ''
                syncMsg["state"] = False
        except Exception as e:
            syncMsg["msg"] = ''
            syncMsg["state"] = False
        self.invokeSync.set(syncMsg)

    def invoke_function(self, params):
        logging.debug("%%%%%%start%%%%%%%%")

        if "invocationType" not in params:
            invocationType = config.INVOCATION_TYPE_SYNC
        else:
            invocationType = params["invocationType"]

        if not (invocationType == config.INVOCATION_TYPE_ASYNC or
                invocationType == config.INVOCATION_TYPE_SYNC):
            logging.error("invalid param2")
            return fc_error.PY_RUNTIME_ERROR_INVAILD_PARAM

        if (not utils.check_param(params, "functionId")):
            if ((not utils.check_param(params, "serviceName")) or
                    (not utils.check_param(params, "functionName")) or
                    (not isinstance(params["serviceName"], str)) or
                    (not isinstance(params["functionName"], str))):
                logging.error("invalid param3")
                return fc_error.PY_RUNTIME_ERROR_INVAILD_PARAM
            serviceName = params["serviceName"]
            functionName = params["functionName"]
            functionId = utils.buildArnString('', '', serviceName, functionName)
        else:
            functionId = params["functionId"]

        if (not isinstance(functionId, str)):
            logging.error("invalid param4")
            return fc_error.PY_RUNTIME_ERROR_INVAILD_PARAM

        if "invokerContext" in params:
            context = params["invokerContext"]
            if (not isinstance(context, str)):
                context_str = json.dumps(context)
            else:
                context_str = context
            context_bytes = base64.standard_b64encode(context_str.encode("utf-8"))
            invokerContext = context_bytes.decode("utf-8")
        else:
            invokerContext = ''

        if "payload" in params:
            if (not (isinstance(params["payload"], str) or
                     isinstance(params["payload"], bytes))):
                logging.error("invalid param5")
                return fc_error.PY_RUNTIME_ERROR_INVAILD_PARAM
            else:
                payload = params["payload"]
        else:
            payload = ''

        msg = self.ipc.invokeTask(functionId, invokerContext, invocationType, payload)
        if invocationType == config.INVOCATION_TYPE_ASYNC:
            if ((msg is not None) and
                    ("msg" in msg)):
                ret = msg["msg"]
                if (("statusCode" in ret) and
                        (ret["statusCode"] == 200) and
                        ("headers" in ret)):
                    header = ret["headers"]
                    # invocationId = header[config.HEADER_INVOCATION_ID]
                    logging.debug("%%%%%%Done%%%%%%%")
                    return "success"
            else:
                return "fail"
        else:
            if ((msg is not None) and
                    ("msg" in msg)):
                # header = msg["msg"]["headers"]        
                # invocationId = header[config.HEADER_INVOCATION_ID]
                # syncMsg = self.ipc.getTaskResult(functionId, invocationId)
                # if (None == syncMsg):
                #     raise fc_error.WSConnException(msg="get task result timeout")
                # ret = None
                ret = msg["msg"]
                if "body" in ret:
                    body = ret["body"]
                else:
                    body = ""
                if "headers" in ret and config.HEADER_FUNCTION_ERROR in ret["headers"]:
                    functionErr = ret["headers"][config.HEADER_FUNCTION_ERROR]
                else:
                    functionErr = ""
                result = {
                    "statusCode": ret["statusCode"],
                    "functionError": functionErr,
                    "payload": body}
                logging.debug("%%%%%%Done%%%%%%%%")
                return result
            else:
                logging.error("invokeTask timeout")
                return None
