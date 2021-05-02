import requests
import time
import os 
os.startfile('telegramA.py')
with open('t.txt','r',encoding='utf8')as ta:
    taa = ta.readlines()
while True:
    for i in taa:
        filee = open('list_Telegram_Id.txt','r').readlines()
        for idd in filee:
            url = f'https://api.telegram.org/bot1630827457:AAHxyYsnRfUIM7XMcU3cvV8_EkE6pB2mWi8/sendMessage?chat_id={idd.strip()}&text={i}'
            r = requests.get(url)
        time.sleep(600)