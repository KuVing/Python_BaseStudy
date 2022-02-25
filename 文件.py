# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:40:52 2021

@author: 15003
"""

def main():
    import os
    a=(os.path.isfile("c:\\Users\\15003\\A.txt"))
    if a==True:
        print("文件存在")
    
    else:
        print("文件不存在")
        
        
   
#    f=open("c:\\Users\\15003\\A.txt","r")
    """data=f.readline()    #一行一行读，每次出一行
    print(data)
    data1=f.readline()
    print(data1)"""
    
    
    """data2=f.readlines()    #一行一行读，一次性输出
    print(data2)"""
    
    
    """while True:
        data=f.read(5)
        print(data)
        if len(data)==0:
            break"""
    
    
#    f.close()
    
#   f=open("c:\\Users\\15003\\A.txt","a")  #如果把a改成w则会覆盖掉原有的东西
#   f.write("\n东鑫宝贝最可爱了")
#   f.close()
 
    with open("c:\\Users\\15003\\A.txt","r")as f1, open("c:\\Users\\15003\\B.txt","a")as f2: #免关闭文件操作
  
        data=f1.read()
        data=data.replace("2","100")
        f2.write(data)
    
    
    pass

if __name__=="__main__":
    main()
    
    
    
    
    
    
    
    
    
    