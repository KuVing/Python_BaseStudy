# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:45:04 2021

@author: 15003
"""

def main():
    a="ABCas a123s sad"
    print(a.capitalize())  #首字母大写
    print(a.swapcase())     #大小写翻转
    print(a.title())         #空格当做单词分界，单词首字母大写
    print(a.center(20,"*"))    #变量居中，不足用*补
    
    b="hahadongxinkeai"
    print(b.startswith("h"))
    print(b.startswith("dongxin",4,11))
    print(b.endswith("i"))
    print(b.find("o"))    
    print(b.replace("a","N",2))  
    print(b.isalpha())   #判断是不是纯字母
    
    c="1231231231231"
    print(c.isnumeric())   #判断是不是纯数字
    
    d="**asdasdasda**"
    print(d.strip("*"))   #去掉左右的*
    print(d.lstrip("*"))
    
    e="192.168.1.12"
    print(e.split("."))   #按.进行分割
     
    pass

if __name__=='__main__':
    main()