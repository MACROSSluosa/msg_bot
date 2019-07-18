#!/usr/bin/python
#-*-coding utf-8-*-
#auther = macrossluosa@icloud.com

import requests
import json
import sys
import os
import time
from datetime import datetime
import xlrd

headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b7762c35-a608-4be3-b80c-7ceb49015ee8"
#api_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ac30155b-431f-4450-b9e9-63de9e826d65"
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

##get the time and format it from excel
# def gettime(nrows,ncols,table):
#     for row in range(0,nrows)
#         verbtime = xlrd.xldate_as_datetime(table.cell(row,0).value,0)
#         if verbtime == 
    

def openexcel(path):
    data = xlrd.open_workbook(path)
    return data



        


if __name__ == '__main__':
    #text = sys.argv[1]
    #text = 'ceshipython'
    #nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    nowtime = time.strftime('%Y.%m.%d',time.localtime(time.time()))

    #nowtime = time.strftime('%Y.%m.%d',time.localtime(time.time()))
    ##open the xlsx
    path1='/Users/mac/pythoncode/msg_bot/msg_checkup/check.xlsx'
    # data1 = xlrd.open_workbook(path1)
    data1 = openexcel(path1)
    #get the first page of excel
    table1 = data1.sheet_by_index(0)
    #表行
    nrows1 = table1.nrows 
    #表列
    ncols1 = table1.ncols
    
    for row in range(0,nrows1):
        #varbtime = xlrd.xldate.xldate_as_datetime(table1.cell(row,0).value, 0)
         varbtime = table1.cell(row,0).value
         print(varbtime)
        #gettime = time.strftime('%Y-%m-%d',varbtime)
         if varbtime == nowtime :
             print('time ok')
             text1  = table1.cell(row,1).value
             text2  = table1.cell(row,2).value
             text = "今天日期是 " + varbtime + text1 + " 帅哥起来巡检机房啦！@" + text2
             msg(text)


    
    



    




    #print(nowtime)
    





