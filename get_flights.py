import urllib
import sys
import time
origin = sys.argv[1]
destination = sys.argv[2] 
print (time.strftime("%Y-%m-%d"))
html = urllib.urlopen('http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?origin='+origin+'&destination='+destination+'&departure_date='+time.strftime("%Y-%m-%d")+'&currency=INR&number_of_results=5&apikey=cYOXzIRsxAPAawOUfb13ZavUPiDmpszM')
get_url = 'http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?origin='+origin+'&destination='+destination+'&departure_date='+time.strftime("%Y-%m-%d")+'&currency=INR&number_of_results=5&apikey=cYOXzIRsxAPAawOUfb13ZavUPiDmpszM'
htmltext = html.read()
print htmltext
print get_url
