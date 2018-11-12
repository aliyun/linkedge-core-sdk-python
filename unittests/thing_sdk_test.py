#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
sys.path.append("../")
sys.path.append("../../../../../lib")
import lecoresdk
import logging
import json
import mock
import unittest
_logger = logging.getLogger(__name__)

ret_params =  {'statusCode': 200, 'payload': 'dHJ1ZQ==', 'functionError': ''}

class TestThingSDK(unittest.TestCase):
    def test_setThingProperties(self):
        it = lecoresdk.IoTData()
        set_params = {"productKey": "a1Kyk5P9XiS",
                      "deviceName": "myfc_light",
                      "payload": {"LightSwitch":0}}
        ret = mock.Mock(return_value = ret_params)
        it.fc.invoke_function = ret
        res = it.setThingProperties(set_params)
        print(res)
        self.assertEqual(res, True)

    def test_getThingProperties(self):
        it = lecoresdk.IoTData()
        get_params = {"productKey": "a1Kyk5P9XiS",
                      "deviceName": "myfc_light",
                      "payload": []}
        # ret_params = {'msg': {'headers': {}, 'statusCode': 200, 'body': 'dHJ1ZQ=='}, 'state': True}
        ret = mock.Mock(return_value = ret_params)
        it.fc.invoke_function = ret
        res = it.getThingProperties(get_params)
        print(res)
        self.assertEqual(res, True)
    
    def test_callThingService(self):
        it = lecoresdk.IoTData()
        srv_params = {"productKey": "a1Kyk5P9XiS",
                      "deviceName": "myfc_light",
                      "service":"upgrade",
                      "payload": {"LightSwitch":1}}
        # ret_params = {'msg': {'headers': {}, 'statusCode': 200, 'body': 'e30='}, 'state': True}
        ret = mock.Mock(return_value = ret_params)
        it.fc.invoke_function = ret
        res = it.callThingService(srv_params)
        print(res)
        self.assertEqual(res, True)

    def test_publish(self):
        it = lecoresdk.IoTData()

        pub_params = {"topic": "/hello/world",
                      "payload": "Hello World! Sent from Linkedge using python"}
        ret = mock.Mock(return_value = ret_params)
        it.fc.invoke_function = ret
        it.publish(pub_params)


    def test_getThingsWithTags(self):
        it = lecoresdk.IoTData()
        get_params = {"payload": []}
        # ret_params = {'msg': {'headers': {}, 'statusCode': 200, 'body': 'W3sicHJvZHVjdEtleSI6ImExS3lrNVA5WGlTIiwiZGV2aWNlTmFtZSI6Im15ZmNfbGlnaHQiLCJ0YWdzIjpbeyJob21lIjoiMTIzIn1dfV0='}, 'state': True}
        ret = mock.Mock(return_value = ret_params)
        it.fc.invoke_function = ret
        res = it.getThingsWithTags(get_params)
        print(res)
        self.assertEqual(res, True)

    def test_setThingProperties_code(self):
        it = lecoresdk.IoTData()
        set_params = {"productKey": "a1Kyk5P9XiS",
                      "deviceName": "myfc_light",
                      "payload": {"key":"value"}}
        # ret_params = {'msg': {'headers': {}, 'statusCode': 202, 'body': 'dHJ1ZQ=='}, 'state': True}
        ret = mock.Mock(return_value = ret_params)
        it.fc.invoke_function = ret
        res = it.setThingProperties(set_params)
        print(res)
        self.assertEqual(res, True)

    def test_invokefunc(self):
        fc_req = lecoresdk.Client()
        invokeParams = {"functionId": "functionId",
                        "invocationType": "Sync",
                        "invokerContext": "{\"custom\": {\"topic\": \"/topic\"}}",
                        "payload": ""}
        
        invoke_params = {'state': True, 'msg': {'statusCode': 200, 'headers': {'X-Fc-Invocation-Id': '1234'}}}
        ret_params = {'msg': {'headers': {}, 'statusCode': 200, 'body': 'e30='}, 'state': True}
        ret_invoke = mock.Mock(return_value = invoke_params)
        fc_req.ipc.invokeTask = ret_invoke
        
        ret = mock.Mock(return_value = ret_params)
        fc_req.ipc.getTaskResult = ret
        res = fc_req.invoke_function(invokeParams)
        print(res)

    def test_invokefunc_name(self):
        fc_req = lecoresdk.Client()
        invokeParams = {"serviceName": "serviceName",
                        "functionName": "functionName",
                        "invocationType": "Sync",
                        "invokerContext": "{\"custom\": {\"topic\": \"/topic\"}}",
                        "payload": ""}
        
        invoke_params = {'state': True, 'msg': {'statusCode': 200, 'headers': {'X-Fc-Invocation-Id': '1234'}}}
        ret_params = {'msg': {'headers': {}, 'statusCode': 200, 'body': 'e30='}, 'state': True}
        ret_invoke = mock.Mock(return_value = invoke_params)
        fc_req.ipc.invokeTask = ret_invoke
        
        ret = mock.Mock(return_value = ret_params)
        fc_req.ipc.getTaskResult = ret
        res = fc_req.invoke_function(invokeParams)
        print(res)

if __name__ == '__main__':
    tc = TestThingSDK()
    tc.test_setThingProperties()
    tc.test_getThingProperties()
    tc.test_callThingService()
    tc.test_publish()
    tc.test_getThingsWithTags()
    tc.test_setThingProperties_code()
    tc.test_invokefunc()
    tc.test_invokefunc_name()
    
