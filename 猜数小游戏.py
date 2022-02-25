# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:07:59 2021

@author: 15003
"""

def main():
    import random
    a=random.randint(0,101)

    b=0
    c=0
    print("请输入你想要猜测的次数：")
    c=int(input(c))
    while b<c:
        guess=int(input("请输入你猜测的数字："))
        if guess>a:
            print("太大了")
            b=b+1
            continue
        
       
        elif guess<a:
            print("太小了")
            b=b+1
            continue
        
       
    
        else: 
            print("你猜对了！")
            break
    if b==c:
        print("所有机会都用完啦，正确答案是：") 
        print(a)
    pass
    input()    
if  __name__=='__main__':
     main()
     
       
    
        
    
       
        

