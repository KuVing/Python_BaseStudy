# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:30:10 2021

@author: 15003
"""

"""def timer(fun):
    def inner(a):
        start=time.time()
        fun(a)
        print(time.time()-start)
    return inner 

@timer
def fun1(a):
    time.sleep(a)
    print("我爱东鑫")
    
def main():
    fun1(5)"""

def timer(fun):
    def inner(*args,**kwargs):
        fun(args,kwargs)
    return inner 

@timer      #在运行装饰器装饰的函数的时候，会把目标函数放入装饰器函数里运行
def fun2(*args,**kwargs):
    print(args,kwargs)
    
def main():
    fun2(123,124,name="dongxin",age="19")
    
    
if __name__=="__main__":
    main()