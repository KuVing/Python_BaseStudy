# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:47:35 2021

@author: 15003
"""

"""def func(a,b):
    def inner(x):
        return a*x+b
    return inner 

def main():
    f=func(4,5)
    f=f(2)
    print(f)"""
import time
def timer(fun):
    def inner():
        start=time.time()
        fun()
        print(time.time()-start)
    return inner
def fun1():
    time.sleep(5)
    print("我爱东鑫")

def main():
    a=timer(fun1)
    a()
    
    

if __name__=="__main__":
    main()