import json , requests
key = 'your Unique key'   # you will get your key from currencylayer.com
currency_url = "http://api.currencylayer.com/live?access_key=" + key
res = requests.get(currency_url)

lst = json.loads(res.text)
new = json.dumps(lst , indent=2)  # you can see structure by printing this value.. 

import smtplib
from twilio.rest import Client

def send_message(account_sid , auth_token):
    try:
        client = Client(account_sid , auth_token)
        message = client.messages.create(body="message.." , from_='twilio_no.' , to='receiver_number') # here from_ is the number from twilio account, to is receiver's no.
        print('Message Sent successfully..')
    except:
        print('Something went wrong while sending message..')

def send_mail(gmail , password):
     try:
        receiver = 'xxxx@gmail.com'
        s=smtplib.SMTP("smtp.gmail.com" , 587)
        s.ehlo()
        s.starttls() ## applying encryption

        s.login(gmail , password) 
        sub = 'Alert mail'
        message = "Bitcoin price just crossed the threshold. \n check the updates immediately."
        s.sendmail(gmail, receiver, 'Subject:{}\n\n{}'.format(sub,message))
        s.quit()
        print("mail sent....")
     except:
        print('Something went wrong while sending mail..')

# calculate btc in INR
import numpy as np
USD_inr = lst['quotes']['USDINR'] 
USD_btc = lst['quotes']['USDBTC']
btc_inr = USD_inr/USD_btc
print(str(np.around(btc_inr , 2)) + ' INR')

gmail = 'xxxxx@gmail.com'    ### sender's gmail.
password = 'your_password'
account_sid ='000000'    # twilio account_sid you can get from your twilio account.
auth_token = 'token..'   # twilio auth_token you can get from your twilio account.

if(np.around(btc_inr , 2) > 500000):    # you can set your own condition.. 
   print('Current bitcoin price is:' + str(np.around(btc_inr , 2)) + ' INR' + '\n' + 'preparing for alert..')
   send_mail(gmail,password)
   send_message(account_sid , auth_token)
   print('Alert Successful')
  
# these are the additional lines of codes which tells you about different currency   

while(True):
    quest = input('Do you want to know about any other currency ?')
    if('yes' in quest.lower()):
       new_cur = input('Enter the currency abbreviation{short form of currency}')
       try:
           if(new_cur.upper() == 'USD'):
                print('1 '+new_cur[-3:] + ' is equal to ' + str(lst['quotes']['USDINR']) + ' INR')
           else:
               new_cur = 'USD' + new_cur.upper()
               USD_cur = lst['quotes'][new_cur] 
               USD_inr = lst['quotes']['USDINR'] 
               output =  USD_inr/USD_cur
               print('1 '+new_cur[-3:] + ' is equal to ' + str(output) + ' INR')
       except:
           print('Invalid Entry. Please Enter valid abbreviation.') 

    else:
        print('Ok bye..')
        break



   
   

   
