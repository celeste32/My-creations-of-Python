# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 17:15:15 2021

@author: abc06
"""

#三角形判斷式
side1 = int(input('請輸入第一個邊長：'))
side2 = int(input('請輸入第二個邊長：'))
side3 = int(input('請輸入第三個邊長：'))
if (side1+side2)>side3 and (side2+side3)>side1 and (side1+side3)>side2:
    if  side1==side2==side3:
        print("這是正三角形")
    elif side1==side2 or side2==side3 or side1==side3:
        if side1*side1+side2*side2==side3*side3 or side2*side2+side3*side3==side1*side1 or side1*side1+side3*side3==side2*side2:
            print("這是等腰直角三角形")
        else:
            print("這是等腰三角形")
    elif side1*side1+side2*side2==side3*side3 or side2*side2+side3*side3==side1*side1 or side1*side1+side3*side3==side2*side2:
        print("直角三角形")
    else:
        print("這是三角形")

else:
    print("這不是三角形")