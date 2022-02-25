# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:29:29 2021

@author: 15003
"""

"""def add():
    b=1               #b=1是最上层的变量

    def c():
        b=10

        def fun():
            nonlocal b    #nonlocal说明不单独赋值，直接用上一层的变量b=10操作
            b=b+20
            print(b)
            
        fun()
        print (b)
        
            
    c()
    
    print(b)

     
def main():
    add()"""

def max(x,y):
    m=x if x>y else y
    return m

def maxmax(a,b,c,d):
    a=max(a,b)
    b=max(c,d)
    c=max(a,b)
    return c
def main():
    d=maxmax(23,124,1231231,12)
    
    print(d)
    
if __name__=="__main__":
    main()