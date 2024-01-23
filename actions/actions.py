# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# In your actions.py file

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from word2number import w2n
import dateparser
from datetime import datetime

class GetInfoAction(Action):

    def name(self) -> Text:
        return "action_get_info"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        # Extract slot values
        slot_values = {
            "temperature": tracker.get_slot("temperature_slot"),
            "precipitation": tracker.get_slot("precipitation_slot"),
            "wind": tracker.get_slot("wind_slot"),
            "humidity": tracker.get_slot("humidity_slot"),
            "sunrise_sunset": tracker.get_slot("sunrise_sunset_slot"),
        }

        # Do something with the dictionary (e.g., log it, return it, etc.)
        # For example, logging the dictionary
        # print(slot_values)
        dispatcher.utter_message("Please wait until I generate your visualization dashboard with the information provided.")
        dispatcher.utter_message("[ACTION SERVER]" + str(slot_values))

        return []


class GetDaysAction(Action):

    def name(self) -> Text:
        return "action_get_days"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get("text")

        dispatcher.utter_message("I ENTERED THE ACTION")
        return [user_input]
        # try:
        #     # Attempt to convert words to numbers
        #     days = w2n.word_to_num(user_input)
        #     message = f"You requested {days} days"
        # except ValueError:
        #     target_date = dateparser.parse(user_input)
        #     if target_date:
        #         current_date = datetime.now()
        #         delta = target_date - current_date
        #         days = delta.days + 2
        #         message = f"You requested {days} days"
        #     else:
        #         days = "Unable to parse your days into an integer"
        # dispatcher.utter_message(message)

        # return [days]