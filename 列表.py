# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 16:00:36 2021

@author: 15003
"""

def main():
    li=["xiaoming","xiaohong","xiaofang"]
    print(li[2])
    li.insert(1,"haha")    #定点增加一个
    print(li)   
    li.append("nihao")   #在最后增加一个
    print(li)
    li.pop()     #去掉最后的
    print(li)
    del li[1:3]    #删除局部
    print(li)
    li.remove("xiaoming")  #定点清除
    print(li)
    li.clear()   #全部清除
    print(li)
    
    lie=["xiaoming","xiaohong","xiaofang"]
    lie[1]="haha"     #定点修改
    print(lie)
    
    
    shuzu=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
    ret=shuzu.count(2)   
    print(ret)
    
    a=shuzu.index(5)
    print(a)
    
    
    
    
    pass


if __name__=="__main__":
    main()