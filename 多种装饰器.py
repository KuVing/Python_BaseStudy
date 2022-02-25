# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:37:37 2021

@author: 15003
"""

"""def outer(flag):
    def time(func):
        def inner(a):
            if flag:
                print("函数开始执行")
                func(a)
                print("函数执行完毕")
            else:
                print("请开启flag")
        return inner 
    return time 
                
@outer(True)

def fun1(a):
    print("haha--",a)
    
def main():
    fun1("东鑫宝贝可可爱爱")"""
    
def wrapper1(func):
    def inner():
        print("装饰器1启动")
        func()
        print("装饰器1结束")
    return inner 

def wrapper2(func):
    def inner():
        print("装饰器2启动")
        func()
        print("装饰器2结束")
    return inner 


@wrapper1 
@wrapper2 

def fun1():
    print("东鑫宝贝可可爱爱")
    
def main():
    fun1()



    
if __name__=="__main__":
    main()
    