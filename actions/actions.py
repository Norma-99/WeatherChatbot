# # This files contains your custom actions which can be used to run

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from word2number import w2n
import dateparser
from datetime import datetime
import spacy



class GetInfoAction(Action):
    """
    Custom Action to get information based on the user's request.
    This action extracts slot values for weather-related parameters and
    sends them back to the user.
    """

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

        dispatcher.utter_message("Please wait until I generate your visualization dashboard with the information provided.")
        dispatcher.utter_message("[ACTION SERVER]" + str(slot_values))

        return []


class ValidateWeatherForm(FormValidationAction):
    """
    Custom Action for form validation in weather-related queries.
    It contains methods to validate the location and days slots
    based on the user's input.
    """

    def name(self) -> Text:
        return "validate_weather_form"
    
    async def validate_location_slot(
        self, 
        slot_value: Any,
        dispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get("text")

        # Load the spaCy model
        nlp = spacy.load("en_core_web_sm")

        # Process the text
        doc = nlp(user_input)

        # Extract entities that are classified as 'GPE' (Geopolitical entity, i.e., countries, cities, states)
        city_names = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
        if city_names:
            dispatcher.utter_message('You requested the weather in ' + str(city_names[0]))
            print(city_names[0])
            return {"location_slot": str(city_names[0])}
        else:
            dispatcher.utter_message('Could not determine the city sorry!')
            return {"location_slot": None}
    

    async def validate_days_slot(
        self, 
        slot_value: Any,
        dispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get("text")

        try:
            # Attempt to convert words to numbers
            days = w2n.word_to_num(user_input)
            message = f"You requested {days} days"
        except ValueError:
            target_date = dateparser.parse(user_input)
            if target_date:
                current_date = datetime.now()
                delta = target_date - current_date
                days = delta.days + 2
                message = f"You requested {days} days"
            else:
                message = "Unable to parse your days into an integer"
                days = None
        dispatcher.utter_message(message)
        return {"days_slot": days}
    