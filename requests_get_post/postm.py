# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     postm
   Description :
   Author :       boytop
   date：          2021/7/20
-------------------------------------------------
   Change Activity:
                   2021/7/20:
-------------------------------------------------
"""
__author__ = 'mild--zwenbo'

import requests
import urllib3
import warnings
urllib3.disable_warnings()

class r_get_post:
    def __init__(self):
        self.url = 'https://standardcs.wx.aipark.com/openapi/bcia/coupon'
        warnings.simplefilter('ignore', ResourceWarning)

    def for_get(self):
        pass

    def for_post(self, databs):
        req = requests.post(url=self.url, json=databs,verify = False)
        req = req.json()
        return req