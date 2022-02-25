# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:51:39 2021

@author: 15003
"""
"""import time
def gen_fun1():
    a=1
    print("将A赋值")
    yield a   #中断函数同时return a
    b=2
    print("将B赋值")
    yield b
    
def main():
    g1=gen_fun1()
    print(next(g1))
    time.sleep(2)
    print(next(g1))"""
def produce():
    for i in range(100):
        yield"生产了%s个包子" %i

def main():
    p=produce()
    num=0

    """for i in range(12):
        print(p.__next__())
        num=num+1"""
    for i in p:
        print(i)    #相当于调用yield
        num=num+1
        if(num==12):
            break
        
       
    
if __name__=="__main__":
    main()