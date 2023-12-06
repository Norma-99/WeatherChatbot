

class ChatbotUI:
    def __init__(self):
        """Initialize the chatbot UI"""
        pass

    def UI_design():
        """This function contains all the frontend design"""
        pass

    def background_design():
        pass

    def dialog_design():
        pass








# import streamlit as st
# import requests

# def get_weather(intent, location, time_interval):
#     # Replace this with the actual URL of your Rasa server
#     rasa_server_url = "http://0.0.0.0:5005"
    
#     data = {
#         "sender": "user",
#         "message": intent,
#         "location": location,
#         "time_interval": time_interval,
#     }

#     response = requests.post(rasa_server_url, json=data)
#     rasa_response = response.json()
    
#     # Extract the weather information from the Rasa response
#     # Adjust this based on the actual structure of your Rasa responses
#     weather_info = rasa_response[0]['text'] if rasa_response else "Sorry, I couldn't understand that."

#     return weather_info

# def main():
#     st.title("Weather Chatbot")

#     intent = st.text_input("Ask for the weather:")
#     location = st.text_input("Enter location (city, country):")
#     time_interval = st.text_input("Enter time interval (e.g., today, tomorrow):")

#     if st.button("Get Weather"):
#         weather_info = get_weather(intent, location, time_interval)
#         st.text("Bot: " + weather_info)

# if __name__ == "__main__":
#     main()
