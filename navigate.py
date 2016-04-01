import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyACBJRuHorzJWpZt6fYfX7vV4H8qB4hxe4')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Infosys Gate 1, 1st Main Rd, Electronics City Phase 1, Electronic City, Bengaluru, Karnataka 560100",
        "Central Silk Board, CSB Complex, B.T.M. Layout, Madivala, Bengaluru, Karnataka 560068",
                                     mode="transit",
                                     departure_time=now)
