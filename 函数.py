# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:50:40 2021

@author: 15003
"""

"""def my_len():
    s='haha nihao'
    length=0
    for i in s:
        length=length+1
    return length,s
   


def main():
    a=my_len()
    print(a)"""

    
def maxnum(x,y=12):
    if x>y:
        max=x
    else:
        max=y
    return max

def main():
    print(maxnum(10,99))
    



if __name__=="__main__":
    main()