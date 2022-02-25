# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file
"""

def main():
    dic={"name":"dongxin","age":"19","JOB":"student"}
   
    
    dic["home"]="tianjin"  #增
    dic.pop("age")         #删
    dic["JOB"]="lose"      #改
    print(dic)
    
    value=dic["name"]      #查
    print(value)
    
    value2=dic.get("name","xxxxxx")
    print(value2)
    
     
    for key,value in dic.items():   #遍历字典
        print(key+"----"+value)
    
    for i in dic:
        print(i)
    for j in dic:
        print(dic[j])
    
    print(dic.keys())
    print(dic.values())
    
if __name__=='__main__':
    main()