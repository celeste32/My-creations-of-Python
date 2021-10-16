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
print(ans)    #此處印出答案供觀看
i=0
while True:
    guess = int(input(f'{min}~{max}請輸入你要猜的數字：'))
    if guess > max or guess < min:
        print("輸入錯誤，請再輸入一次")
        continue
    i += 1
    if guess != ans and i<5:
        if guess < ans:
            min = guess
            print("目前已猜了{0}次，請再猜一次".format(i))
        else:
            max = guess
            print("目前已猜了{0}次，請再猜一次".format(i))
    elif guess == ans and i<5:
        print('恭喜猜對了')
        
    if i ==5 and guess != ans:
        print('已猜錯5次，下次再來')
        
    elif i == 5 and guess == ans:
        print('恭喜猜對了')
        
        r = str(input("是否要繼續遊玩？(Y/N)"))
        r = str(r)
        r.upper()
        if r == 'Y':
            ans = random.randint(1,100)
            i=0    
            continue
        elif r == 'N':
            break
        r.upper()
        while r != 'Y' or r != 'N':
            r = str(input('輸入錯誤，請重新再輸入一次：'))
            r = str(r)
            #結束迴圈
        