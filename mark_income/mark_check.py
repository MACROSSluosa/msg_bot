#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os 
import requests
import json
import sys
import time
##
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
                "18866878526"
            ],
            "isAtAll": False
        }
    }
    ## 这是python2的语法；python3的要修改
    #print requests.post(api_url,json.dumps(json_text),headers=headers).content
    print(requests.post(api_url,json.dumps(json_text),headers=headers).content)

#if __name__ == '__main__':
#    text = sys.argv[1]
#   msg(text)
##

if __name__ == "__main__":
    while True:
        print('the conding will be run')
   
        filepath01 = "./"
        #list00 = list_name(filepath00)
        list01 = os.listdir(filepath01)
        #testtime = time.localtime(time.time())
        testtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        text = "收益目标管控放舱采集命令文件异常,时间是 " + testtime

    
        #使用 os.path.splitext(file)[0] 可获得 文件名 。 
        #使用 os.path.splitext(file)[-1] 可获得以 . 开头的 文件后缀名 。

        countRun = 0
        for file in list01:
            #print(file)
            b =  os.path.splitext(file)[1]
            if b == ".RUN":
                countRun = countRun + 1 
        
        if countRun > 1:
            print("采集指令文件异常")
            msg(text)

        else:
            print("Everthing is ok!")



        time.sleep(60)

    
    




    
