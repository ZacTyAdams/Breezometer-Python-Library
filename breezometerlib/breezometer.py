import json
from json.encoder import py_encode_basestring
import requests

class Breezometer:
    """
    This object will act as our object for which to retrieve and hold information

    :param latitude: latitude for place of interest
    :param longitude: longitude for place of interest
    :param apiKey: breezometer api obtained from the developer site
    """

    def __init__(self, latitude: str, longitude: str, apiKey: str) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.apiKey = apiKey

    def test_connection(self):
        """
        This function tests connection to the Breezometer API using the 3 essential Params: latitude, longitude, apiKey

        The specific call made for this test is a GET call to the /air-quality/v2/current-conditions endpoint

        :return: Response code of GET call
        :rtype: int
        """
        response = requests.get(
                    "https://api.breezometer.com/air-quality/v2/current-conditions",
                    params={"lat": self.latitude, "lon": self.longitude, "key": self.apiKey},
                )
        return response.status_code 
    
    def get_current_aqi(self):
        """This function returns all the following features related to the current AQI in the object's specified lat/long coordinates
        
        breezometer_aqi,local_aqi,health_recommendations,pollutants_concentrations,pollutants_aqi_information

        :return: Returns the response from the call (this is also saved to Breezometer.current_aqi)
        :rtype: dict
        """
        try:
            response = requests.get(
                        "https://api.breezometer.com/air-quality/v2/current-conditions",
                        params={"lat": self.latitude, "lon": self.longitude, "key": self.apiKey, "features": "breezometer_aqi,local_aqi,health_recommendations,pollutants_concentrations,pollutants_aqi_information"},
                    )
            if response.status_code != 200:
                raise Exception(response.status_code)
        except(Exception):
            print("Issue making call to Breezometer: " + Exception)

        if not response:
            raise ConnectionAbortedError("Update failed due to invalid response from Breezometer")
        else:
            self.current_aqi = response.json()["data"]
            return self.current_aqi

    def get_aqi_forecast(self, hours=96):
        """
        This function returns hourly air-quality forecasts for the specified location. Each forecast includes hourly air quality indexes, pollutant data, and health recommendations for a maximum of 96 hours (4 days).
        
        Features: breezometer_aqi,local_aqi,health_recommendations,pollutants_concentrations,pollutants_aqi_information

        :param hours: Number hours you wish to look ahead (max 96)
        :type hours: int

        :return: Returns the response from the call (this is also saved to Breezometer.aqi_forcast)
        :rtype: List of dict       
        """
        try:
            response = requests.get(
                        "https://api.breezometer.com/air-quality/v2/forecast/hourly",
                        params={"lat": self.latitude, "lon": self.longitude, "key": self.apiKey, "hours": hours, "features": "breezometer_aqi,local_aqi,health_recommendations,pollutants_concentrations,pollutants_aqi_information"},
                    )
            if response.status_code != 200:
                raise Exception(response.status_code)
        except(Exception):
            print("Issue making call to Breezometer: " + Exception)

        if not response:
            raise ConnectionAbortedError("Update failed due to invalid response from Breezometer")
        else:
            self.aqi_forecast = response.json()["data"]
            return self.aqi_forecast

    def get_pollen_forecast(self, days=3):
        """
        This function returns daily forecast pollen conditions for a specific location. Each daily forecast includes daily pollen index for types and plants for a maximum of 3 days (current day and two following days).
        
        Features: types_information,plants_information

        :param days: Number from 1 to 3 that indicates how many days forecast to request
        :type days: int

        :return: Returns the response from the call (this is also saved to Breezometer.aqi_forcast)
        :rtype: List of dict       
        """
        try:
            response = requests.get(
                        "https://api.breezometer.com/pollen/v2/forecast/daily",
                        params={"lat": self.latitude, "lon": self.longitude, "key": self.apiKey, "features": "types_information,plants_information", "days": days},
                    )
            if response.status_code != 200:
                print("Error in response: " + response.status_code)
                print(response.reason)
                raise Exception(response.status_code)
        except(Exception):
            print("Issue making call to Breezometer: " + str(Exception.args))
        if not response:
            raise ConnectionAbortedError("Update failed due to invalid response from Breezometer")
        else:
            self.pollen_forecast = response.json()["data"]
            return self.pollen_forecast