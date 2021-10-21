# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 01:33:48 2021

@author: abc06
"""
"""
105261363：作品－－終極密碼
"""
import random

ans = random.randint(1,100)
max = 100
min = 1
i = 0
#print(ans)  # 此處印出答案供觀看

while True:
    guess = int(input(f'目前已猜了{i}次，在{min}~{max}中請輸入你要猜的數字：'))
    if guess > max or guess < min:
        print("輸入錯誤，請再輸入一次")
        continue
    i += 1
    if guess==ans:
        print('恭喜猜對了')
        r = input("是否要繼續遊玩？(Y/N)").upper()
        if r == 'Y':
            max=100
            min=1
            ans = random.randint(1,100)
            i=0
            continue
        else:
            break
    elif guess < ans:
        min = guess
    else:
        max = guess

    if i == 5:
        print('已猜錯5次，下次再來')
        r = input("是否要繼續遊玩？\n若要繼續，請按Y，不繼續請按任意鍵").upper()
        if r == 'Y':
            max=100
            min=1
            ans = random.randint(1,100)
            i=0
            continue
        else:
            break
    
