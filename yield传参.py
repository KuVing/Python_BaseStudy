# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:41:36 2021

@author: 15003
"""

def gen():
    print(123)
    content=yield 1 #中断，return1，外面send东西给content
    print(content)
    print(456)
    yield 2
    
def main():
    
    g=gen()
    ret1=g.__next__()
    print("第一个yield是：",ret1)
    ret2=g.send("鑫宝可可爱爱")#给第一个yield发东西发完自动执行next
    
    print("第二个yield是：",ret2)
    
if __name__=="__main__":
    main()
    
    