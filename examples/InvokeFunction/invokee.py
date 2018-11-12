# -*- coding: utf-8 -*-
import logging  
import lecoresdk


def handler(event, context):
  logging.debug(event)
  logging.debug(context)
  return 'hello world'
