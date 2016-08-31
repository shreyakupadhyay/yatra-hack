import urllib
import sys
import time
import json
import MySQLdb
db = MySQLdb.connect('localhost','root',*******,'yatra')
cursor = db.cursor()
origin = sys.argv[1]
destination = sys.argv[2] 
print (time.strftime("%Y-%m-%d"))
html = urllib.urlopen('http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?origin='+origin+'&destination='+destination+'&departure_date='+time.strftime("%Y-%m-%d")+'&currency=INR&number_of_results=5&apikey=cYOXzIRsxAPAawOUfb13ZavUPiDmpszM')
#get_url = 'http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?origin='+origin+'&destination='+destination+'&departure_date='+time.strftime("%Y-%m-%d")+'&currency=INR&number_of_results=5&apikey=cYOXzIRsxAPAawOUfb13ZavUPiDmpszM'
htmltext = json.loads(html.read())


val_res = len(htmltext['results'])
#val_ite = len(htmltext['results'][0]['itineraries'])
#print len(htmltext['results'][0]['itineraries'][0]['outbound'])
#sql = """DROP TABLE IF EXISTS user_info (
 #               dep_time char(30),
 #               arr_time char(30),
 #               airline char(30),
 #               flight_no char(30),
 #               seats_avail char(30),
 #               total_price char(30),
 #               refundable char(30) )"""
#cursor.execute(sql)
for j in range(0,val_res):
    val_ite = len(htmltext['results'][j]['itineraries'])
    for i in range(0,val_ite):
        print "departure time" , htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['departs_at']
        dep_time = htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['departs_at']
        print "arrival time" , htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['arrives_at']
        arr_time = htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['arrives_at']
        print "origin" , htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['origin']['airport']
        origin = htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['origin']['airport']
        print "terminal" , htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['origin']['terminal']
        terminal = htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['origin']['terminal']
        print "destination" , htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['destination']['airport']
        destination = htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['destination']['airport']
        print "aircraft" , htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['aircraft']
        aircraft = htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['aircraft']
        print "airlines" , htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['operating_airline']
        airline = htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['operating_airline']
        print "flight number" , htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['flight_number']
        flight_no = htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['flight_number']
        print "travel class" , htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['booking_info']['travel_class']
        tra_class = htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['booking_info']['travel_class']
        print "booking code" , htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['booking_info']['booking_code']
        book_code = htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['booking_info']['booking_code']
        print "seats available" , htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['booking_info']['seats_remaining']
        seats_avail = htmltext['results'][j]['itineraries'][i]['outbound']['flights'][0]['booking_info']['seats_remaining']
        print "total_price" , (htmltext['results'][j]['fare']['total_price'])
        total_price = (htmltext['results'][j]['fare']['total_price'])
        print "refundable" , (htmltext['results'][j]['fare']['restrictions']['refundable'])
        refundable = (htmltext['results'][j]['fare']['restrictions']['refundable'])
        try:
            cursor.execute("""INSERT INTO information VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(dep_time,arr_time,origin,terminal,destination,aircraft,airline,flight_no,tra_class,book_code,seats_avail,total_price,refundable))
            db.commit()
        except:
            db.rollback()

db.close()

