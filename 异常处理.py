# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:57:54 2021

@author: 15003
"""

def main():
    """try:
        a=1
        b=0
        c=a/b
    except:
        print("程序出错了！")"""
    
    
    s1="Index" 
    try:
      print("你真棒")
      raise ValueError("必然的啦！")
    except ValueError as e:
        print("ValueError",e)
    except KeyError as e:
        print("KeyError",e)
    except IndexError as e:
        print("IndexError",e)   
    except Exception as e:
        print("未知异常")
    finally:
        print("Finally 结束了！")
    
        
    
        
if __name__=="__main__":
    main()
