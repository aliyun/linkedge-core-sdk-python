# -*- coding: utf-8 -*-
import logging  
import oss2
import lecoresdk


cred = lecoresdk.CredentialProviderChain().get_credential()
logging.debug(cred)
auth = oss2.StsAuth(cred['accessKeyId'], cred['accessKeySecret'], cred['securityToken'])
bucket = oss2.Bucket(auth, 'http://oss-cn-shanghai.aliyuncs.com', 'test-iotedge')
bucket_info = bucket.get_bucket_info()
logging.debug('name: ' + bucket_info.name)
logging.debug('storage class: ' + bucket_info.storage_class)
logging.debug('creation date: ' + bucket_info.creation_date)
logging.debug('intranet_endpoint: ' + bucket_info.intranet_endpoint)
logging.debug('extranet_endpoint ' + bucket_info.extranet_endpoint)
logging.debug('owner: ' + bucket_info.owner.id)
logging.debug('grant: ' + bucket_info.acl.grant)
bucket.put_object_from_file('abcd.txt', '/root/text.txt')

def handler(event, context):
  pass
  
