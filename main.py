
from alright import WhatsApp
import time
import pandas as pd


df = pd.read_excel('data.xlsx')
df['PHONE'] = df['PHONE'].astype(str)
numbers = df['PHONE'].to_list()
numbers = list(set(numbers))

msg = """
Your text
"""

# numbers = ['905XXXXXXX']
messenger = WhatsApp()
counter = 0
try:
    for number in numbers:
        messenger.find_user(number)
        time.sleep(2)
        messenger.send_picture("./image.png","Image message")
        time.sleep(2)
        messenger.send_message(msg)
        counter+=1
        print(counter)
        time.sleep(2)
        
except:
    print(str(counter)," message sent, ERROR!")
time.sleep(60)

