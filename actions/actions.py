# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

# class ActionGreet(Action):
#     def name(self) -> Text:
#         return "action_greet"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_greet")
#         return []

# class ActionGetTemperature(Action):
#     def name(self) -> Text:
#         return "action_get_temperature"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Replace with your logic to fetch temperature data
#         dispatcher.utter_message("Here is the temperature information.")
#         return []



class ActionSetResponse(Action):
    def name(self) -> Text:
        return "action_set_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Set the 'response_type' variable based on the user's response
        affirm_intent = tracker.latest_message['intent'].get('name') == 'affirm'
        response_type = tracker.get_slot('response_type')  # Change 'response_type' to the appropriate slot name
        tracker.events.append(SlotSet(response_type, affirm_intent))

        return []



# class ActionGetPrecipitation(Action):
#     def name(self) -> Text:
#         return "action_get_precipitation"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Replace with your logic to fetch precipitation data
#         dispatcher.utter_message("Here is the precipitation information.")
#         return []

# class ActionGetWind(Action):
#     def name(self) -> Text:
#         return "action_get_wind"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Replace with your logic to fetch wind data
#         dispatcher.utter_message("Here is the wind information.")
#         return []

# class ActionGetHumidity(Action):
#     def name(self) -> Text:
#         return "action_get_humidity"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Replace with your logic to fetch humidity data
#         dispatcher.utter_message("Here is the humidity information.")
#         return []

# class ActionGetSunriseSunset(Action):
#     def name(self) -> Text:
#         return "action_get_sunrise_sunset"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Replace with your logic to fetch sunrise and sunset data
#         dispatcher.utter_message("Here is the sunrise and sunset information.")
#         return []

# class ActionGetLocation(Action):
#     def name(self) -> Text:
#         return "action_get_location"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         location = tracker.get_slot("location")
#         # Replace with your logic to fetch weather data for the specified location
#         dispatcher.utter_message(f"Here is the weather information for {location}.")
#         return []

# class ActionGetDays(Action):
#     def name(self) -> Text:
#         return "action_get_days"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         days = tracker.get_slot("days")
#         # Replace with your logic to fetch weather data for the specified number of days
#         dispatcher.utter_message(f"Here is the weather forecast for the next {days} days.")
#         return []

# class ActionGetWeatherType(Action):
#     def name(self) -> Text:
#         return "action_get_weather_type"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         weather_type = tracker.get_slot("weather_type")

#         if weather_type:
#             dispatcher.utter_message(f"Great! I'll provide information about {weather_type}.")
#         else:
#             dispatcher.utter_message("I'm sorry, I didn't understand the weather type you're asking for.")

#         return []