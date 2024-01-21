# class NLPTraining:
#     def __init__():
#         pass


import spacy
from spacy.matcher import Matcher
from word2number import w2n

nlp = spacy.load("en_core_web_sm")

def extract_location(user_input):
    matcher = Matcher(nlp.vocab)
    location_pattern = [[{"ENT_TYPE": "GPE"}]]
    matcher.add("LOCATION", location_pattern)

    doc = nlp(user_input)
    matches = matcher(doc)
    
    for match_id, start, end in matches:
        if nlp.vocab.strings[match_id] == "LOCATION":
            return doc[start:end].text
    
    return None

def extract_days(user_input):
    doc = nlp(user_input)
    for token in doc:
        try:
            # Attempt to convert words to numbers
            return w2n.word_to_num(token.text)
        except ValueError:
            pass
        if token.like_num:
            return int(token.text) 
    return None

def extract_weather_preferences(user_input):
    matcher = Matcher(nlp.vocab)
    patterns = [
        [{"LOWER": {"in": ["temperature", "warmth", "hot", "cold"]}, "OP": "?"}],
        [{"LOWER": {"in": ["precipitation", "rain", "snow"]}, "OP": "?"}],
        [{"LOWER": {"in": ["wind", "breeze"]}, "OP": "?"}],
        [{"LOWER": {"in": ["humidity", "moisture"]}, "OP": "?"}],
        [{"LOWER": {"in": ["sunrise", "sunset", "daylight"]}, "OP": "?"}],
    ]
    matcher.add("WEATHER_PREFERENCES", patterns)
    doc = nlp(user_input)
    matches = matcher(doc)
    return {doc[start:end].text.lower(): True for _, start, end in matches}

def process_user_input(user_input: dict):
    extracted_data = {
        "location": extract_location(user_input),
        "days": extract_days(user_input),
        **extract_weather_preferences(user_input)
    }

    return extracted_data

# Example usage:
user_input = {
    'location': 'i live in tokio',
    'days': 'the next four days',
    'temperature': 'I would like to know the temperature',
    'precipitation': 'sure',
    'wind': 'not interested', 
    'humidity': 'absolutely',
    'sunrise_sunset': 'yeah'
}
user_input2 = ""
for key in user_input:
    user_input2 += f"{key} {user_input[key]}, "

print(user_input2)
# user_input = "I want to know the weather in London for the next 4 days with temperature, precipitation, wind, humidity, and sunrise/sunset."
example_user_resp = process_user_input(user_input2)
print(example_user_resp)

expected_response = {
    "location": "tokio",
    "days": 4,
    "temperature": True,
    "precipitation": True,
    "wind": False,
    "humidity": True,
    "sunrise_sunset": True
}
