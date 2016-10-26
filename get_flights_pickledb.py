import urllib , sys , time , json , MySQLdb , random , pickledb

db = MySQLdb.connect('localhost','root',***********,'yatra')
session_id = random.randint(100000000,999999999)

cursor = db.cursor()

origin = sys.argv[1]
destination = sys.argv[2] 

print (time.strftime("%Y-%m-%d"))

response = urllib.urlopen('http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?origin='+origin+'&destination='+destination+'&departure_date='+time.strftime("%Y-%m-%d")+'&currency=INR&number_of_results=5&apikey=cYOXzIRsxAPAawOUfb13ZavUPiDmpszM')
#get_url = 'http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?origin='+origin+'&destination='+destination+'&departure_date='+time.strftime("%Y-%m-%d")+'&currency=INR&number_of_results=5&apikey=cYOXzIRsxAPAawOUfb13ZavUPiDmpszM'
responseText = json.loads(response.read())


val_res = len(responseText['results'])
def createTable():
	sql = """DROP TABLE IF EXISTS user_info (
	               dep_time char(30),
	               arr_time char(30),
	               airline char(30),
	               flight_no char(30),
	               seats_avail char(30),
	               total_price char(30),
	               refundable char(30) )"""
	cursor.execute(sql)

picl = pickledb.load('test.db',False)
row = []
for j in range(0,val_response):
    len_responseText = len(responseText['results'][j]['itineraries'])
    
    for i in range(0,len_responseText):
        dep_time = iterate_json(i,j,responseText)['departs_at']
        print "departure time" , dep_time

        arr_time = iterate_json(i,j,responseText)['arrives_at']
        print "arrival time" , arr_time

        origin = iterate_json(i,j,responseText)['origin']['airport']
        print "origin" , origin

        terminal = iterate_json(i,j,responseText)['origin']['terminal']
        print "terminal" , terminal

        destination = iterate_json(i,j,responseText)['destination']['airport']
        print "destination" , destination

        aircraft = iterate_json(i,j,responseText)['aircraft']
        print "aircraft" , aircraft
        
        airline = iterate_json(i,j,responseText)['operating_airline']
        print "airlines" , airline

        flight_no = iterate_json(i,j,responseText)['flight_number']
        print "flight number" , flight_no

        tra_class = iterate_json(i,j,responseText)['booking_info']['travel_class']
        print "travel class" , tra_class

        booking_code = iterate_json(i,j,responseText)['booking_info']['booking_code']
        print "booking code" , booking_code

        seats_avail = iterate_json(i,j,responseText)['booking_info']['seats_remaining']
        print "seats available" , seats_avail

        total_price = (responseText['results'][j]['fare']['total_price'])
        print "total_price" , total_price

        refundable = (responseText['results'][j]['fare']['restrictions']['refundable'])
        print "refundable" , refundable

        try:
            cursor.execute("""INSERT INTO information VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(dep_time,arr_time,origin,terminal,destination,aircraft,airline,flight_no,tra_class,book_code,seats_avail,total_price,refundable))
            db.commit()
        except:
            db.rollback()
        rd = (dep_time,arr_time,origin,terminal,destination,aircraft,airline,flight_no,tra_class,book_code,seats_avail,total_price,refundable)
        row.append(rd)
db.close()

picl.set(session_id,row)
print picl.get(session_id)
picl.dump()
