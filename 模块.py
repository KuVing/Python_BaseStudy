# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:47:45 2021

@author: 15003
"""

"""import test1 

def main():
   test1.fun1()"""

"""import test1 as x   #取别名
def main():
    x.fun2()"""

"""from test1 import *   #如果test1里限定all=fun1，那就只能调用fun1
def main():
    fun2()"""
from test1 import fun1
def main():
    fun1()



if __name__=="__main__":
    main()
    