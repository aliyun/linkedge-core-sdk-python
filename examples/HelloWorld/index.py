# -*- coding: utf-8 -*-
import logging  
import lecoresdk
import time


it = lecoresdk.IoTData()
pub_params = {"topic": "/topic/hello",
              "payload": "hello world"}
while True:
  time.sleep(5)
  it.publish(pub_params)
  print("publish success")

def handler(event, context):

  return 'hello world'
