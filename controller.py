### IMPORTS
import streamlit as st
import requests
import ast

from weather_information import WeatherInformation
from viz_dash import VisualizationDashboard
from chatbotUI import ChatbotUI


class ChatbotController:
    def __init__(self, endpoint_url:str = "http://0.0.0.0:5005/webhooks/rest/webhook"):
        """initialize the chatbot framework"""
        self.endpoint_url = endpoint_url
        print(f"Endpoint: {self.endpoint_url}")
        self.responses = dict()
        st.title("Weather Chatbot")

        with st.chat_message(name="assistant"):
            st.markdown("Hey I am your AI based assistant")

        # Setting up the session state with a loop that shows the conversation
        # In the chat message I can add my own avatar if I want
        if "messages" not in st.session_state:
            st.session_state.messages = []
    

    def process_interaction(self, prompt):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        body_json = {
            'sender': 'streamlit',
            'message': prompt
        }

        post_response = requests.post(self.endpoint_url, json=body_json)
        post_response_json = post_response.json()
        print(post_response)
        print(post_response_json)

        if post_response: 
            bot_response = [elem['text'] for elem in post_response_json]
        
        with st.chat_message("assistant"):
            for response in bot_response:
                if response.startswith("[ACTION SERVER]"):
                    self.update_responses(response=response)
                else: 
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.markdown(response)


    def update_responses(self, response: str) -> None:
        """Every time we get a response we update the vizualisation info"""
        # Find the start and end indices of the dictionary
        try: 
            splits = response.split(']')
            split = splits[1]
            json_response = ast.literal_eval(split.replace("'", "\""))
            self.responses = json_response
            ## CHANGE THIS IN THE FUTURE
            self.responses['location'] = 'Amsterdam'
            self.responses['days'] = 7
        except: 
            raise Exception(f"The response message is not in the correct format. Response: {response}")
        self.get_final_visualization_dashboard()



    def get_final_visualization_dashboard(self):
        """Once the questions are done show a visualization dashboard"""
        wi = WeatherInformation(self.responses)
        info = wi.get_weather_info()

        print(info)
        vd = VisualizationDashboard(info)
        plots = vd.run()

        chat_UI = ChatbotUI(plots, info["location"], info['days'])
        chat_UI.display_plots()


    def run(self):
        # Print the whole conversation
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Get user input and chatbot output
        if prompt := st.chat_input("Type your query"):
            self.process_interaction(prompt=prompt)

        


###### GOAL #######
# example_user_resp = {
#     "location": "london",
#     "days": 4,
#     "temperature": True,
#     "precipitation": True,
#     "wind": True,
#     "humidity": True,
#     "sunrise_sunset": True
# }