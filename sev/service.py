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

from http.server import BaseHTTPRequestHandler
import json


from sev import lqxq_set_id


class Resquest(BaseHTTPRequestHandler):
    def handler(self):
        print("data:", self.rfile.readline().decode())
        self.wfile.write(self.rfile.readline())

    def do_GET(self):
        print(self.requestline)
        if self.path == '/hello':
            self.send_error(404, "Page not Found!")
            return

        data = {
            'result_code': '10000',
            'result_desc': 'Success',
            'timestamp': '',
            'data': {'message_id': '25d55ad283aa400af464c76d713c07ad'}
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        print(self.headers)
        print(self.command)
        self.req_datas = self.rfile.read(int(self.headers['content-length']))  # 重点在此步!
        self.req_datas = json.loads(self.req_datas.decode())
        if self.path == "/api/capital/carInPush.jsp":

           print("入场订单推送:{}".format(self.req_datas))

        elif self.path == "/api/capital/carOutPush.jsp":

           print("出场订单推送:{}".format(self.req_datas))

        else:

           print("其他路径：{}".format(self.req_datas))

        data = {
            'result_code': '10000',
            'result_desc': '请求成功',
            'data': []
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        lqxq_set_id.L().I_req(self.req_datas['CAR_NUM'],self.req_datas['ORDER_ID'])  # 接口请求


