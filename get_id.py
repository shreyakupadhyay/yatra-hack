import urllib ,sys , json , os, time

API_KEY = '*******************'

response = urllib.urlopen('http://api.sandbox.amadeus.com/v1.2/airports/autocomplete?apikey='+API_KEY +'&term='+ sys.argv[1])

responseText = json.loads(response.read())

all_prf = len(responseText)
info_origin = []
for i in range(0,all_prf):
    info_origin.append(responseText[i]['value'])
    info_origin.append(responseText[i]['label'])
    os.system('python /home/shreyakupadhyay/Documents/yatra-hackathon/get_flights.py ' + str(responseText[i]['value']) + ' ' + 'BLR')
