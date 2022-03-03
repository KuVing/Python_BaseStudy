# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:01:31 2021

@author: 15003
"""

"""def fun1():
    print("abcdefg")

def main():
    f=fun1
    print(f)
    
    f()"""

def fun1():
    print("abcdefg")

def fun2():
    print("hijklmn")

def fun3():
    print("opqrst")
    
def main():
    li=[fun1,fun2,fun3]
    dic={"hanshu1":fun1,"hanshu2":fun2,"hanshu3":fun3}
    
    li[0]()
    dic["hanshu3"]()
    
if __name__=="__main__":
    main()
