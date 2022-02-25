# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 16:09:21 2021

@author: 15003
"""

set1={1,2,3,4,5,6,7,8,3,3,3,3,3,3,3}

set1.add("dongxin")
print(set1)
set1.remove(3)
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)

set2={7,8,1,9}
set3={1,2,3,4,5,6,7,8,4,21,2,10}

print(set2 & set3)
print(set2 | set3)
print(set2-set3)
print(set3-set2)
print(set2^set3)
