# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:16:00 2021

@author: abc06
"""
import os
import requests
from bs4 import BeautifulSoup
my_url = "https://www.books.com.tw/web/sys_saletopb/books"
data = requests.get(my_url)
data.encoding = "UTF-8"
data = data.text
books = BeautifulSoup(data,"html.parser")

Step1 = books.find_all("li",class_="item")

for i in Step1:
    rank = i.find("strong").text
    h4 = i.find('h4')
    title = h4.find('a').text
    link = h4.find('a').get('href')
    print(rank,title,link,end="\n")
    
os.system("pause")