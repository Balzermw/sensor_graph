# We're importing json to read the json response from the server. We import requests to communicate with the server via API
import json
import requests

from datetime import datetime
# Grab editable settings from our settings.py. This includes the sensor ID
from settings import Constants

class TemperatureSensor():

    # Constructor
    def __init__(self, group_id, sensor_id):
        self.sensor_id = sensor_id  # ID of the sensor (used in API Request)
        self.group_id = group_id  # Group ID of the sensor (used in API Request)
        self.name = ""  # Name of the sensor (Retrieved from the API Response)
        self.vehicleId = ""  # ID of the vehicle (Retrieved from the API Response)
        self.y = []  # The temperature values (Plotted on y axis)
        self.x = []  # The time that the temperature was recorded (Plotted on x axis)

    # since the server is responding with celcius we need to convert to farenheit
    def toFahrenheit(self, celsius):
        return (celsius * (9.0 / 5.0)) + 32

        #We're formatting the request to begin to grab data from the server
    def sense(self):
        # POST Request's Body
        body = {
            "groupId": self.group_id,
            "sensors": [self.sensor_id]
        }

        # Request's Query Parameter (appended to URL after ?)
        params = {
            "access_token": Constants.access_token
        }

        # Sending a POST request to the temperature API URL/Endpoint
        response = requests.post(Constants.temperature_end_point, params=params, json=body)

        # If response status code is not 200 OK, something is wrong, so raise exception
        if response.status_code != 200:
            raise Exception("Non OK Response from Server. Response:\n" + response.text)

        # Parse response as json (to dictionary)
        response = response.json()

        # Extract data from dictionary and set it as object's properties
        sensor_data = response["sensors"][0]
        # grabbing name and vehicleID from the reqest
        self.name = sensor_data["name"]
        self.vehicleId = sensor_data["vehicleId"]
        # based on the api_time_format we entered in settings we're creating the graph
        time = datetime.strptime(sensor_data["ambientTemperatureTime"], Constants.api_time_format)
        self.x.append(time.strftime("%d-%b-%y %H:%M"))
        # we're converting milicelcius to celicus
        temp = sensor_data["ambientTemperature"] / 1000.0
        #converting temp to farenheit (human readable)
        self.y.append(self.toFahrenheit(temp))
    # import the length setting to start graphing
    def get_graphing_data(self, length):
        self.sense()
        return self.x[-length:], self.y[-length:]
