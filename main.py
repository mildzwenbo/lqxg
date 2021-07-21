# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     lqxgservice
   Description :
   Author :       boytop
   date：          2021/7/19
-------------------------------------------------
   Change Activity:
                   2021/7/19:
-------------------------------------------------
"""
__author__ = 'mild--zwenbo'
import sys,os
from os import path
d = path.dirname(__file__) # 获取当前路径
parent_path = os.path.dirname(d) # 获取上一级路径
sys.path.append(parent_path+"//webservice//sev") # 如果要导入到包在上一级


from sev import service
from http.server import HTTPServer

if __name__ == '__main__':
    host = ('', 8088) # 指定端口号啊啊
    server = HTTPServer(host, service.Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()