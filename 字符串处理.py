# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 21:35:07 2021

@author: 15003
"""

def main():
    
    a="abcdefgasdasghkvbkghjchgFZxz"
    print(a[0])
    print(a[0:3])   #从第零个开始取三个
    print(a[2:])    #从第三个开始
    print(a[2:-1])  #从第三个开始取到倒数第二个，第三个和倒数第二个都要
    print(a[2:7:2]) #从三个开始到第七个取出，步长为2
    
    
    pass

if __name__=="__main__":
    main()