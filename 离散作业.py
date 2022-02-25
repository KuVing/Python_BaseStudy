# -*- coding: utf-8 -*-
"""

"""
def main():
    result=0
    c=1
    a=int(input("输入你想要的连接符个数："))
    b=[] 
    while(a):
        lianjiefu=input("输入你想要的连接符：")
        b.append(lianjiefu)
        a=a-1
    
    for i in b:
        if(c == 1):
            if (i == "AND"):
                result=1
            else:
                result=3
        
        if(c>=2):
            if (i == "AND"):
                result=result
            else:
                result=2**c+result
            
        c=c+1
    
    print("最终结果是：",result)
    
    
if __name__=="__main__":
    main()
    input()
    
