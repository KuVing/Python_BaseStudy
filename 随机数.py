# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 08:36:43 2021

@author: 15003
"""

"""import random
def main():
     print(random.random())
     print(random.uniform(0,4))  #生成一个0-4之间的小数
     print(random.randint(1,5))   #生成1-5之间的整数,不包括5
     print(random.randrange(1,10,2)) #生成1-10之间的奇数
     
     a,b=random.sample(["梅花A","红方块Q","红桃2","黑方块K","红桃6"],2)
     print(a,b)   #随机输出两个
     
     item=["梅花A","红方块Q","红桃2","黑方块K","红桃6"]
     random.shuffle(item)
     print(item)     #相当于洗牌"""

import random   
def v_code():
    code=""
    for i in range(4):
        num=random.randint(0,4)
        alf=chr(random.randint(65,91))   #根据ascll码转出大写字母
        add=random.choice([num,alf])
        code="".join([code,str(add)])  #在0-9和A-Z中随机生成一个
    return code

def main():     #生成验证码
    a=v_code()
    print(a)
     

     
if __name__ =="__main__":
    main()