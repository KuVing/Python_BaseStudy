# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:01:31 2021

@author: 15003
"""

"""def fun1():
    print("东鑫宝贝超级可爱")

def main():
    f=fun1
    print(f)
    
    f()"""

def fun1():
    print("谢翔宇喜欢东鑫宝贝")

def fun2():
    print("东鑫宝贝喜欢谢翔宇")

def fun3():
    print("谢翔宇和东鑫宝贝喜欢彼此")
    
def main():
    li=[fun1,fun2,fun3]
    dic={"hanshu1":fun1,"hanshu2":fun2,"hanshu3":fun3}
    
    li[0]()
    dic["hanshu3"]()
    
if __name__=="__main__":
    main()