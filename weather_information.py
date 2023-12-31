import random
from datetime import datetime, timedelta


class WeatherInformation:
    def __init__(self, user_resp: dict):
        self.user_resp = user_resp
        self.weather_information = dict()

    def get_weather_info(self):
        """
        Look at each variable if True or False and build the weather information variable with mock data"""
        convertor = {
            "temperature": self.get_temperatures,
            "precipitation": self.get_precipitations,
            "wind": self.get_winds,
            "humidity": self.get_humidities,
            "sunrise_sunset": self.get_sunrises_and_sunsets
        }
        for key in list(self.user_resp.keys()):
            if self.user_resp[key] == True:
                self.weather_information[key] = convertor[key]()
            else:
                self.weather_information[key] = None
        self.weather_information["location"] = self.user_resp["location"]
        self.weather_information["days"] = self.user_resp["days"]

    def get_temperatures(self) -> list:
        """
        Get the temperature of the days assigned in the user_resp variable in the location selected.
        Return: a list of temperatures for each day.
        """
        return [random.randint(0, 30) for _ in range(self.user_resp['days'])]

    def get_precipitations(self) -> list:
        """
        Get the precipitations mm of the days assigned in the user_resp variable in the location selected.
        Return: a list of precipitations for each day.
        """
        return [random.uniform(0, 10) for _ in range(self.user_resp['days'])]

    def get_winds(self) -> list:
        """
        Get the velocity of the winds of the days assigned in the user_resp variable in the location selected.
        Return: a list of the winds for each day.
        """
        return [random.uniform(0, 20) for _ in range(self.user_resp['days'])]

    def get_humidities(self) -> list:
        """
        Get the humidity percentage of the days assigned in the user_resp variable in the location selected.
        Return: a list of humidities for each day.
        """
        return [random.randint(0, 100) for _ in range(self.user_resp['days'])]

    def get_sunrises_and_sunsets(self):
        """
        Get random but consistent sunrise and sunset times for the days assigned in the user_resp variable in the location selected.
        Return: a list, containing the sunrises and the sunsets for each day.
        """
        sunrise_times = [self.generate_random_time(6, 8) for _ in range(self.user_resp['days'])]
        sunset_times = [self.generate_random_time(18, 20) for _ in range(self.user_resp['days'])]
        return [(sunrise.strftime("%I:%M%p"), sunset.strftime("%I:%M%p")) for sunrise, sunset in zip(sunrise_times, sunset_times)]

    def generate_random_time(self, start_hour, end_hour):
        """
        Generate a random time between start_hour and end_hour.
        Return: a datetime object representing the generated time.
        """
        random_hour = random.randint(start_hour, end_hour)
        random_minute = random.randint(0, 59)
        return datetime(1, 1, 1, random_hour, random_minute) + timedelta(days=random.randint(0, 365))




# Example usage
example_user_resp = {
    "location": "london",
    "days": 4,
    "temperature": True,
    "precipitation": True,
    "wind": True,
    "humidity": True,
    "sunrise_sunset": True
}
weather_info = WeatherInformation(example_user_resp)
weather_info.get_weather_info()

print(weather_info.weather_information)