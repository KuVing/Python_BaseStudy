# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:59:19 2021

@author: 15003
"""

"""def fun1(name,age,*args):
    print("name:",name)
    print("age:",age)
    print("*args:",args)
    print("第一个额外变量:",args[0])
    
def main():
    t=("dongxin","19","student","xiexiangyu")
    fun1(*t)"""
    
"""def fun2(**dic):
    print(dic)
    
def main():
    dic={"name":"dongxin","age":"19"}
    fun2(**dic)"""

"""def fun1(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

def main():
    
    dic={"name":"dongxin","age":"18"}
    fun1(1,2,3,4,5,**dic)
    fun1(1,2,3,4,5,name="dongxin",age="19")"""
    
def main():
    x=lambda y,z:y**z
    print(x(2,3))

if __name__=="__main__":
    main()