import requests
from pprint import pprint
GS_ENDPOINT = "https://api.sheety.co/e7c2f4008393f98c66fd03bd4457319e/flightDeals/prices"
authorization = {"Authorization":"Bearer flightdealsearchengine"}

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def getData(self):
        res = requests.get(url=GS_ENDPOINT, headers=authorization)
        data = res.json()
        self.destination_data = data["price"]
        return self.destination_data

    def updateData(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{GS_ENDPOINT}/{city['id']}", json=new_data, headers=authorization)

            print(response.text)
