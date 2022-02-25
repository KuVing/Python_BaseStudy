# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:00:57 2021

@author: 15003
"""

"""import json
def main():
    dic={"k1":"v1","k2":"v2"}
    str=json.dumps(dic)
    print(str)
    print(type(str))
    print(type(dic))
    
    dic1=json.loads(str)
    print(dic1)"""

"""import hashlib      #哈希加密
def main():
    md5=hashlib.md5()#进行md5加密
    md5.update('东鑫好可爱'.encode('utf-8'))
    print(md5.hexdigest())"""





"""import configparser #修改配置文件
def main():
    conf=configparser.ConfigParser()
    conf['default']={'money':1005,'weapon':'yes'}
    conf['home']={'island':'xiaodao1'}
    with open(".\config","w")as f:
        conf.write(f)     #配置文件写入"""



"""import configparser
def main():
    conf=configparser.ConfigParser()
    conf.read("config")    #读取config
    print("home" in conf)    #判断是否存在
    for key in conf["default"]:
        print(key)
    print(conf.get("default","money"))   #获取某个键的值
    print(conf.items("default"))  #获取所有键值对
    print(conf.options("default")) #获取所有键
    conf.add_section("tank")    #增加键
    conf.remove_section("home")   #删除键
    conf.remove_option("default","weapon")   #删除条目
    conf.set("default","money","999")   #修改条目
    conf.write(open("conf.new","w"))"""
    
"""from collections import namedtuple       #定义坐标系
def main():
    point=namedtuple("zuobiao",["x","y"])
    p=point(20,30)
    print(p.x)"""

"""import time
def main():
    print("start")
    time.sleep(2)
    print("end")
    print(time.time())
    print(time.strftime("%Y-%m-%d %X")) #输出当前时间
    print(time.strftime("%Y/%m/%d %H:%M:%S"))"""

import datetime
import time
def main():
    now=datetime.datetime.now()
    print(now)
    print(datetime.datetime.now()+datetime.timedelta(weeks=3))  #三周后
    print(now.replace(year=1972,month=10,day=21))   #时间调整
    sjc=time.time()
    print(datetime.datetime.fromtimestamp(sjc))   #将时间戳转为当前时间
    
    



    
    
    
    
if __name__ =="__main__":
        main()