import requests
from data_manager import DataManager
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "oG9fa8kjineRt2635ymwU4zb0uIrEuuF"
kiwi_ID = "patryk4150flightdeals"

SEARCH_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    def get_destination_code(self, city_name):
        loc_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name}
        respond = requests.get(url=loc_endpoint, headers=headers, params=query)
        results = respond.json()["locations"]
        code = results[0]['code']
        return code

    def find_destination_price(self, from_fly_code, to_fly_code, date_from, date_to):
        dst_endpoint = f"{SEARCH_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"fly_from": from_fly_code, "max_stopovers": 0, "fly_to": to_fly_code, "dateFrom": date_from, "dateTo": date_to}
        respond = requests.get(url=dst_endpoint, headers=headers, params=query)


        try:
            data = respond.json()['data'][0]
        except IndexError:
            print("There's no flights")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport_code=data["cityCodeTo"],
            departure_city=data["cityTo"],
            departure_airport_code=data["cityCodeTo"],
            out_date=data["route"][0],
            return_date=data["route"]
        )
        print(f"{flight_data.departure_city}: {flight_data.price} Euro")
        return flight_data


