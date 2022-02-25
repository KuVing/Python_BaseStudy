# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:38:42 2021

@author: 15003
"""

"""def squard(x):  #函数列表推导式
    return x**2

def main():
    mul=[squard(i) for i in range(30) if i%3 ==0]
    print(mul)"""
    

"""def main():    多重列表推导
    fruits=[["apple","banana"],["watermelon","coconut"]]
    print([name for a in fruits for name in a if name.count("a")>=2])"""
def main():
    dic1={"a":1,"b":2}
    dic2={dic1[k]:k for k in dic1}
    print(dic2)
"""def main():     #集合推导式

    li=[1,2,3,4,-1,-2]
    s={x**2 for x in li}
    print(s)"""
    

if __name__=="__main__":
    main()