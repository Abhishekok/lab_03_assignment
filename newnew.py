flight_table = [
    {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},{"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
    {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},{"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
    {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},{"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499},
]

city_codes = {
    "BLR": "Bengaluru","BOM": "Mumbai","BBI": "Bhubaneswar","HYD": "Hyderabad","JLR": "Jabalpur"}

def sfbc(cid):
    print("Flights for", city_codes[cid] + ":")
    for flight in flight_table:
        if flight["From"] == cid or flight["To"] == cid:
            print("Flight ID:", flight['Flight ID'], "From:", city_codes[flight['From']] "To:", city_codes[flight['To']] , "Price:", flight['Price'])

def sffc(cid):
    print("Flights from", city_codes[cid] + ":")
    for flight in flight_table:
        if flight["From"] == cid:
            print("Flight ID", flight['Flight ID'] , "To", city_codes[flight['To']] , "Price ", flight['Price'])

def search_flights_between_cities(cid1, cid2):
    print("Flights between", city_codes[cid1], "and", city_codes[cid2] )
    for flight in flight_table:
        if flight["From"] == cid1 and flight["To"] == cid2:
            print("Flight ID:", flight['Flight ID'], "Price:", flight['Price'])

print("Search options:")
print("1. Flights for a particular City")
print("2. Flights From a city")
print("3. Flights between two given cities")
print("4. Exit")
    
choice = input("Enter choice")
    
if choice == '1':
    cid = input("Enter cid")
    sfbc(cid)
elif choice == '2':
    cid = input("Enter cid")
    sffc(cid)
elif choice == '3':
    cid1 = input("Enter first cid: ")
    cid2 = input("Enter 2nd cid: ")
    search_flights_between_cities(cid1, cid2)
elif choice == '4':
    print("Exiting the program.")
else:
    print("Invalid choice.")