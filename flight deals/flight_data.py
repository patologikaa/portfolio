import datetime


class FlightData:
    def __init__(self, price, origin_city, origin_airport_code, departure_airport_code, departure_city,
                 out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport_code = origin_airport_code
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.out_date = out_date,
        self.return_date = return_date


