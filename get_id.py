import urllib
import sys
import json
import os
import time
API_KEY = '*******************'

html = urllib.urlopen('http://api.sandbox.amadeus.com/v1.2/airports/autocomplete?apikey='+API_KEY +'&term='+ sys.argv[1])

htmltext = json.loads(html.read())

print htmltext 
all_prf = len(htmltext)
info_origin = []
for i in range(0,all_prf):
    info_origin.append(htmltext[i]['value'])
    info_origin.append(htmltext[i]['label'])
    os.system('python /home/shreyakupadhyay/Documents/yatra-hackathon/get_flights.py ' + str(htmltext[i]['value']) + ' ' + 'BLR')
