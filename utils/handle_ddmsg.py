# -*- coding: utf-8 -*-
# -------------------------
# @Time    :  2023/6/27 9:11
# @Author  : alvin
# @Description:  发送钉钉消息
# -------------------------
import configparser
import datetime
import hmac
import hashlib
import base64
import urllib.parse
from utils.handle_path import config_path_ini
import requests
import json
from urllib3 import encode_multipart_formdata
import time



def send_ding_msgs(msg,myself=None):
    # print("config_path", config_path_ini)
    config = configparser.ConfigParser()
    config.read(config_path_ini, encoding="utf-8-sig")
    headers = {'Content-Type': 'application/json', "Charset": "UTF-8"}
    # print(config.get('url','API_FEAR'))
    if myself is None:
        secret = config.get("dingding", 'SECRET')
        # 这里替换为复制的完整 webhook 地址
        send_access_token = config.get("dingding", 'ACCESS_TOKEN')
    else:
        send_access_token = config.get("dingding", 'ACCESS_TOKEN_MYSELF')
        # 这里替换为自己复制过来的加签秘钥
        secret = config.get("dingding", 'SECRET_MYSELF')
    prefix = "https://oapi.dingtalk.com/robot/send?access_token={}".format(send_access_token)
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    url = f'{prefix}&timestamp={timestamp}&sign={sign}'

# 钉钉消息格式，其中 msg 就是我们要发送的具体内容
    data = {
        "at": {
            "isAtAll": False
        },
        "text": {
            "content": msg
        },
        "msgtype": "text"
    }
    # print("msg",msg)
    return requests.post(url=url, data=json.dumps(data), headers=headers).text
    # return 1


if __name__ == "__main__":
    # pass
    # # 填写你的钉钉机器人secret和access_token
    symbol_price_history = ['BTC', 'ETH']
    baibeisymbol_price = {'IOTX':0.038,'ZKF':0.01,'PYTH':0.4,'BONK':0.0000099,'BAKE':0.45,'MUBI':0.13,'SATS':0.00000075,'ONDO':0.32,'SEI':0.6}
    # send_ding_msgs("百倍币持仓币种数量:{},成本价:{}".format(len(baibeisymbol_price), baibeisymbol_price))
    send_ding_msgs("百倍币持仓币种数量:{},成本价:{}".format(len(baibeisymbol_price), baibeisymbol_price))