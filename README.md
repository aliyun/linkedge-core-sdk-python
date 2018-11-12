# Link IoT Edge Core SDK for Python

The package allows developers to write functions on Function Compute using python, which running within Link IoT Edge.


## Example

Here is a examle demonstrates publishing messages to a topic.

``` python
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

# don't remove this function
def handler(event, context):
  return 'hello world'
```

## APIs

* [IoTData#**publish()**](#publish)
* [IoTData#**getThingProperties()**](#getThingProperties)
* [IoTData#**setThingProperties()**](#setThingProperties)
* [IoTData#**callThingService()**](#callThingService)
* [IoTData#**getThingsWithTags()**](#getThingsWithTags)
* [Client#**invoke_function()**](#invokeFunction)
* [CredentialProviderChain()#**get_credential()**](#getCredential)

---

<a name="publish"></a>
### IoTData.publish(params)
Publishes messages.

The parameters are:

* params`dict`: which contains:
	* topic`str`(Required): the topic name to be published.
	* payload`str|bytes`(Required): the message payload in string or in binary.

---

<a name="getThingProperties"></a>
### IoTData.getThingProperties(params)
Obtains specific properties of a thing.

The parameters are:

* params`dict`: which contains:
	* productKey`str`(Required): the productKey of the target thing from which to get properties.
	* deviceName`str` (Required) the deviceName of the target thing from which to get properties.
	* payload`list`(Required): a list of keys that specifies the properties to be obtained.
* return:
	* code`int`: if success it will return 0, or return error code.
	* output`dict`: return values. eg:{'property1':xxx, 'property2':yyy, ...}.

---
<a name="setThingProperties"></a>
### IoTData.setThingProperties(params)
Updates the properties of a thing.

The parameters are:

* params`dict`: which contains:
	* productKey`str`(Required): the productKey of the target thing to which to set properties.
	* deviceName`str`(Required): the deviceName of the target thing to which to set properties.
	* payload`dict`(Required): a dict consisting of keys and values that specifies the properties to be updated.eg, {"property1": "xxx", "property2": "yyy", ...}.
* return: 
	* code`int`: if success it will return 0, or return error code.
	* output`dict`: customer data，if no data, it will return {}.

---
<a name="callThingService"></a>
### IoTData.callThingService(params)
Calls a specific service of a thing.

The parameters are:

* params`dict`: which contains:
	* productKey`str`(Required): the productKey of the target thing of which to call a service.
	* deviceName`str`(Required): the deviceName of the target thing of which to call a service.
	* service`str`(Required): the name of the service to be called.
	* payload`str|bytes`: a optional string or binary in JSON that you provided to the service as arguments.
* return:
	* code`int`: if success it will return 0, or return error code.
	* output`dict`: return values. eg:{"key1": "xxx", "key2": "yyy", ...}.  

---
<a name="getThingsWithTags"></a>
### IoTData.getThingsWithTags(params)
Obtains a list of thing objects, each of which being with all given tags.

The parameters are:

* params`dict`: which contains:
	*  payload`list`(Required): a list of `tag` that consisting of dict `{key: value}`. eg:[{"key":"value"}]
* return:
	* contains a list of device match the tags. eg, [{"productKey":"xxx", "deviceName":"yyy"}].

---
<a name="invokeFunction"></a>
### Client.invoke_function(params)
Invokes a specific function.

The parameters are:

* params`dict`: which contains:
	* functionId`str`(Required): the id of the function to be invoked. Function name is not supported currently.
	* invocaionType`str`: a optional type of the invocation, may be `Sync` or `Async`. It will be `Sync` if not specified.
	* invokerContext`str`: a optional invoker-specific information to the invoked function. The invoker information will be passed into the function, and can be choosed through context variable. It must be base64-encoded.
	* payload`str|bytes`: a optional string or binary data that you want to provide to the function as input.

---
<a name="getCredential"></a>
### CredentialProviderChain().get_credential()
get [credential data](https://help.aliyun.com/document_detail/28765.html?spm=a2c4g.11186623.6.683.773125fbZIUFnC).

* return`dict`: get credential data. eg, {"accessKeyId":"xxx", "accessKeySecret", "yyy", "securityToken", "zzz"}
	


## License
Apache 2.0
