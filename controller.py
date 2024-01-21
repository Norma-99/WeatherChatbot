### HELPFUL INFORMATION
#   HELPFUL VIDEO: https://www.youtube.com/watch?v=skKNjq0QL-4

### IMPORTS
import streamlit as st
from rasa.core.agent import Agent
import asyncio
import requests

# from weather_information import WeatherInformation
# from viz_dash import VisualizationDashboard
# from chatbotUI import ChatbotUI


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
            'sender': 'streamlit2',
            'message': prompt
        }

        post_response = requests.post(self.endpoint_url, json=body_json)
        post_response_json = post_response.json()
        print(post_response)
        print(post_response_json)

        if post_response: 
            bot_response = post_response_json[0]['text']
        
        with st.chat_message("assistant"):
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            self.update_responses(user_input=prompt, response=bot_response)
            st.markdown(bot_response)


    def update_responses(self, user_input: str, response: str) -> None:
        """Every time we get a response we update the vizualisation info"""
        pass


    def get_user_input(self, prompt: str) -> None:
        """Retrieves the user's input"""
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)


    async def get_chatbot_response(self, prompt:str) -> None:
        print(f"User's input: {prompt}")
        response = await self.agent.handle_text(prompt)
        print(f"Chatbot's response: {response}")
        bot_response = "There was no response from the model"
        if response: 
            bot_response = response[0]['text']
        
        with st.chat_message("assistant"):
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            self.update_responses(user_input=prompt, response=bot_response)
            st.markdown(bot_response)
            
        # with st.chat_message("assistant"):
        #         ### DO HERE THE CHATBOT LOGIC
        #         st.session_state.messages.append({"role": "assistant", "content": prompt})
        #         self.update_responses(user_input=prompt, response=prompt)
        #         st.markdown(prompt)


    def get_final_visualization_dashboard():
        """Once the questions are done show a visualization dashboard"""
        pass


    def run(self):
        # Print the whole conversation
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Get user input and chatbot output
        if prompt := st.chat_input("Type your query"):
            self.process_interaction(prompt=prompt)
            # self.get_user_input(prompt=prompt)
            # asyncio.run(self.get_chatbot_response(prompt=prompt))
        
        # At the end of the answers print the visualization dashboard
        # wi = WeatherInformation(self.responses)
        # wi.get_weather_info()

        # vd = VisualizationDashboard(wi)
        # plots = vd.run()

        # chat_UI = ChatbotUI(plots, wi["location"], wi['days'])
        # chat_UI.display_plots()


###### GOAL #######
example_user_resp = {
    "location": "london",
    "days": 4,
    "temperature": True,
    "precipitation": True,
    "wind": True,
    "humidity": True,
    "sunrise_sunset": True
}