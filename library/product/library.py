#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver # chromeを操作するため
from selenium.webdriver.chrome.options import Options # オプションを使うために必要
from selenium.webdriver.common.by import By # chromeを操作するため
from time import sleep # 待機のため

import datetime # 時間を取得する
import smtplib # メールサーバーを操作してメールを送信する
# SMTP メールを送信するための通人のルール
import ssl # 暗号化や認証の仕組みを使う
from email.mime.text import MIMEText # メールを日本語で送信できるようにする

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout, encoding='utf-8')

from password.id_password import *


# In[2]:


option = Options()                          # オプションを用意
option.add_argument('--headless')           # ヘッドレスモードの設定を付与
chromedriverPath = "/Users/imainaoya/Downloads/chromedriver"
browser = webdriver.Chrome(chromedriverPath ,options=option)
# browser = webdriver.Chrome()

url = "https://www.meguro-library.jp/opw/OPS/OPSUSER.CSP"
browser.get(url)

cardnumber_xpath = "/html/body/div/section/form/article[2]/div/ul/li[1]/input"
elem_username = browser.find_element(By.XPATH, cardnumber_xpath)
elem_username.send_keys(library_ID)

password_xpath = "/html/body/div/section/form/article[2]/div/ul/li[2]/input"
elem_username = browser.find_element(By.XPATH, password_xpath)
elem_username.send_keys(library_PASSWORD)

# login_button_xpath = "/html/body/div/section/form/article[3]/div/ul/li[3]/a"
# elem_login_btn = browser.find_element(By.PARTIAL_LINK_TEXT, login_xpath)
# これだけはpythonからjavascriptを動かす構文
# https://python-auto.com/2020/02/10/%E3%80%90python3%E3%83%BB%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0%E3%80%91-a%E3%82%BF%E3%82%B0%E3%81%8C%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E5%87%BA%E6%9D%A5%E3%81%AA%E3%81%84/
browser.execute_script('javascript:GoLogin("../OPS/OPSUSERLOGIN.CSP")')
# elem_login_btn.click()

user_page_xpath = "/html/body/div/div[1]/nav/li[2]/a"
user_page_btn = browser.find_element(By.XPATH, user_page_xpath)
user_page_btn.click()

lending_xpath = "/html/body/div/section[2]/article[3]/ul/li[1]/a"
lendeig_page_btn = browser.find_element(By.XPATH, lending_xpath)
lendeig_page_btn.click()

subject = "目黒区立図書館の図書の返却期限が迫っています。"
body = ""
# <br>は改行

books = browser.find_elements(By.CLASS_NAME, 'item')
for i in range(len(books)):
    s = books[i].text
    # print(s)
    # print(type(books[i].text))
    # print('タイトル' in s)
    # print(s.find('タイトル'))
    number_title = s.find('タイトル')
    number_kind = s.find('種別')
    string_title = s[number_title+5:number_kind-1]
    body += "　署名　　：" + string_title + "<br>"
    # print(string_title)
    # print(s.find('貸出日'))
    number_loanDate = s.find('貸出日')
    string_loanDate = s[number_loanDate+4:number_loanDate+14]
    body += "　貸出日　：" +  string_loanDate + "<br>"
    # print(string_loanDate)
    # print(s.find('返却期限日'))
    number_returnDeadline = s.find('返却期限日')
    string_returnDeadline = s[number_returnDeadline+6:number_returnDeadline+16]
    body += "返却期限日：" + string_returnDeadline + "<br>" + "<br>"
    # print(string_returnDeadline)
    # print('貸出日' in s)
    # print('返却期限日' in s)

sleep(10)

browser.quit()


# In[3]:


body


# In[4]:


import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout, encoding='utf-8')

gmail_account = str(google_ID)
gmail_password = str(google_PASSWORD)
mail_to = str(google_ID)
send_name = 'なおや'

mail_to

# today_date = datetime.date.today()
# delivary_date = today_date + datetime.timedelta(days=7)

msg = MIMEText(body, "html")
# msg

msg["Subject"] = subject
msg["To"] = mail_to
msg["From"] = gmail_account
# msg


# In[5]:


server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
server.login(gmail_account, gmail_password)
server.send_message(msg)
server.close()
'送信完了'


# In[ ]:




