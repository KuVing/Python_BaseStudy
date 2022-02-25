# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:28:37 2021

@author: 15003
"""

"""from collections  import Iterable

def main():
    l=[1,2,3,4]
    print(isinstance(l,Iterable))"""   #判断是否可以迭代
    
def main():
    li=[1,2,3,4,5]
    a=iter(li)
    while True:
        try:
           
            print(next(a))
        except:
           print("迭代结束")
           break

if __name__=="__main__":
    main()