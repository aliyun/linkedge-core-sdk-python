# -*- coding: utf-8 -*-
import logging  
import lecoresdk

def handler(event, context):
  it = lecoresdk.IoTData()
  set_params = {"productKey": "YourProductKey",
                "deviceName": "YourDeviceName",
                "payload": {"LightSwitch":0}}
  res = it.setThingProperties(set_params)
  print(res)
  get_params = {"productKey": "YourProductKey",
                "deviceName": "YourDeviceName",
                "payload": ["LightSwitch"]}
  res = it.getThingProperties(get_params)
  print(res)
  pub_params = {"topic": "/topic/hello",
                "payload": "hello world"}
  it.publish(pub_params)
  print("publish success")
  get_params = {"payload": [{"home":"123"}]}
  res = it.getThingsWithTags(get_params)
  print(res)
  get_params = {"productKey": "YourProductKey",
                "deviceName": "YourDeviceName",
                "service":"upgrade",
                "payload": {"LightSwitch": 0}}
  res = it.callThingService(get_params)
  print(res)
  return 'hello world'
