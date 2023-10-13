# 프로젝트 사용중 필요한 부분만 커스텀하여 사용
from FlightRadar24 import FlightRadar24API

class FrAPIHandler(FlightRadar24API):

    def __init__(self):
        print(FlightRadar24API)
        self.fr_api = FlightRadar24API()
        self.flights = self.fr_api.get_flights()

    def frapi_now_flight_position(self) -> list:

        return self.flights

    def frapi_now_path_flight_line(self, flight) -> dict:

        return self.fr_api.get_flight_details(flight)

