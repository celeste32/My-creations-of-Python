1012# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 17:09:09 2021

@author: abc06
"""

i = int(input('輸入一個正整數：'))
count = 0

for n in range(2,i):
    if i % n == 0:
        print('此數為合數')
        break
        count += 1
    elif n == i-1 :
        print("此數為質數")
        break
    if i == 2 :
        print('此數為質數')
else:
    print("此數既非質數，也非合數")