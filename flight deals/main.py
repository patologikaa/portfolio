import datetime

import data_manager
import flight_data
from flight_search import FlightSearch

DM = data_manager.DataManager()
sheet_data = DM.getData()

MY_DESTINATION = "KRK"

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    DM.destination_data = sheet_data
    DM.updateData()

now_date = (datetime.datetime.now()).strftime("%d/%m/20%y")
future_date = (datetime.datetime.now() + datetime.timedelta(weeks=40)).strftime("%d/%m/20%y")

for destination in sheet_data:
    flight = FlightSearch.find_destination_price(MY_DESTINATION, destination["iataCode"], now_date,future_date)
