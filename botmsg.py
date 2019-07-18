#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
####
#脚本可以适用；执行脚本需要带参数 如下例子
#./dingding.py 123
#适用与python3和python2 
#需要修改对应的环境变量

import requests
import json
import sys
import os

headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ac30155b-431f-4450-b9e9-63de9e826d65"

def msg(text):
    json_text= {
     "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": [
                "1881***1223"
            ],
            "isAtAll": False
        }
    }
    ## 这是python2的语法；python3的要修改
    #print requests.post(api_url,json.dumps(json_text),headers=headers).content
    print(requests.post(api_url,json.dumps(json_text),headers=headers).content)

if __name__ == '__main__':
    #text = sys.argv[1]
    text = 'ceshipython' 
    msg(text)
