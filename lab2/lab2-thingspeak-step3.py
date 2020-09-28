#This code was taken from the youtube video by soumil (given in lab 2 document)
import urllib.request
import requests
import threading
import json

import random

def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/1161383/feeds.json?api_key=H8CSN1W6VDYYVW9K&results=2'
  
    print(URL)

    get_data=requests.get(NEW_URL).json()
    print(get_data)
    channel_id=get_data['channel']['id']

    feild_1=get_data['feeds']
    print(feild_1)

    t=[]
    for x in feild_1:
       t.append(x['field1']) 
       print(x['field1'])
        

