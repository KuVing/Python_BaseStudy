# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:19:49 2021

@author: 15003
"""

"""def outer(a):
    b=10
    def inner():
        print(a+b)
    print(inner.__closure__)  #闭包返回CELL,不是的话就是NONE
    return inner   #一个函数定义中引用了函数外定义的变量，并且该函数可以在其定义环境外被执行。
                   #这样的一个函数我们称之为闭包
    

def main():
    a=outer(10)
    a()"""
    
def waihanshu():
    money=10000
    
    def zhongjianhanshu():
        name="dongxin"
        
        def inner():
            print(money,name)
        return inner
    return zhongjianhanshu

def main():
    a=waihanshu()
    i=a()
    i()

if __name__=="__main__":
    main()