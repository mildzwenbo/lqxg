# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     lqxq_set_id
   Description :
   Author :       boytop
   date：          2021/7/20
-------------------------------------------------
   Change Activity:
                   2021/7/20:
-------------------------------------------------
"""
__author__ = 'mild--zwenbo'

from requests_get_post import postm
merchantNo  =   "lqxgvaluecard"
partner     =   "lqxg"

class L(postm.r_get_post):

    def I_req(self, carNum, orderId):
        couponId_list_name = ""
        orderInfo = {
            "service"       :       "tcroute.parkinginfo.orderInfo",
            "carNum"        :       carNum,
            "freeMins"      :       "0",
            "version"       :       "1.0",
            "merchantNo"    :       merchantNo,
            "sign"          :       "3347b109a1e44f3fd5baa78b74a84948",
            "partner"       :       partner,
            "timestamp"     :       "2021-05-25 09:52:34",
            "charset"       :       "utf-8",
            "signType"      :       "md5"
        }
        out_datas = {
            "service"       :       "tcroute.parkinginfo.outParkOrder",
            "method"        :       "parkfee.outParkOrder",
            "orderId"       :        orderId,
            "merchantNo"    :        merchantNo,
            "version"       :       "1.0",
            "sign"          :       "3347b109a1e44f3fd5baa78b74a84948",
            "partner"       :       partner,
            "timestamp"     :       "2021-05-25 09:52:34",
            "charset"       :       "utf-8",
            "signType"      :       "md5"
        }
        selectBindOrderByOrderId = {
            "service": "merchant.coupon.selectBindOrderByOrderId",
            "orderId": orderId,
            "version": "1.0",
            "sign": "3347b109a1e44f3fd5baa78b74a84948",
            "partner": "lqxg",
            "merchantNo": merchantNo,
            "timestamp": "2021-05-25 09:52:34",
            "charset": "utf-8",
            "signType": "md5"
        }
        selectBindOrderByCarNum = {
            "service"          :        "merchant.coupon.selectBindOrderByCarNum",
            "merchantNo"       :        merchantNo,
            "carNum"           :        carNum,
            "version"          :        "1.0",
            "sign"             :        "3347b109a1e44f3fd5baa78b74a84948",
            "partner"          :        partner,
            "timestamp"        :        "2021-05-25 09:52:34",
            "charset"          :        "utf-8",
            "signType"         :        "md5",
            "verifyIgnore"     :        "true"
        }
        while True:
            bh = input("1({})2({})3({})4({})5({})6({})7({})q({})\ninput：\n".format(
                "在场订单查询", "出场订单查询", "为在场车订单绑定优惠券","查询优惠券订单使用信息",
                "根据停车订单ID查询优惠券订单使用信息","根据车牌号查询绑定优惠券记录", "优惠券解绑", "退出"))

            if bh == '1':
                print(self.for_post(orderInfo))
            elif bh == '2':
                print(self.for_post(out_datas))
            elif bh == '3':
                couponType = input('couponType:  2:停车券费全免，5:金额券，6:时间券')
                couponNum = input('couponNum:  优惠券类型为时间，传入优惠时长(单位分);优惠券类型为金额，传入 优惠金额;停车费全免则空字符串 ')
                bindCoupon = {
                    "service": "merchant.coupon.bindCoupon",
                    "orderId": orderId,
                    "merchantNo": "lqxgvaluecard",
                    "couponType": couponType,  # 优惠券类型(2:停车券费全免，5:金额券，6:时间券)
                    "couponNum": couponNum,  # 优惠券类型为时间，传入优惠时长(单位分);优惠券类型为金额，传入 优惠金额;停车费全免则空字符串   N
                    "isTimeoutFree": "1",
                    "version": "1.0",
                    "sign": "3347b109a1e44f3fd5baa78b74a84948",
                    "partner": "lqxg",
                    "timestamp": "2021-05-25 09:52:34",
                    "charset": "utf-8",
                    "signType": "md5"
                }
                couponId = self.for_post(bindCoupon)
                if couponId['returnMsg'] == 'OK':
                    print(couponId['couponId'])
                    couponId_list_name = couponId['couponId']
                else:
                    print(couponId['returnMsg'])

            elif bh == '4':
                find_bind_datas = {
                    "service": "merchant.coupon.selectBindOrder",
                    "couponId": couponId_list_name,
                    "version": "1.0",
                    "merchantNo": merchantNo,
                    "sign": "3347b109a1e44f3fd5baa78b74a84948",
                    "partner": "lqxg",
                    "timestamp": "2021-05-25 09:52:34",
                    "charset": "utf-8",
                    "signType": "md5"
                }
                print(self.for_post(find_bind_datas))
            elif bh == '5':
                print(self.for_post(selectBindOrderByOrderId))

            elif bh == '6':
                print(self.for_post(selectBindOrderByCarNum))  # 开始时间 结束时间

            elif bh == '7':
                unBindCoupon = {
                    "service": "merchant.coupon.unBindCoupon",
                    "couponId": couponId_list_name,
                    "version": "1.0",
                    "sign": "3347b109a1e44f3fd5baa78b74a84948",
                    "partner": "lqxg",
                    "merchantNo": merchantNo,
                    "timestamp": "2021-05-25 09:52:34",
                    "charset": "utf-8",
                    "signType": "md5",
                }
                print(self.for_post(unBindCoupon))
            elif bh == 'q':
                print("退出")
                break
            else:
                print("\033[5;31m 输入值错误请重新输入 \033[0m")

