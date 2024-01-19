### HELPFUL INFORMATION
#   HELPFUL VIDEO: https://www.youtube.com/watch?v=skKNjq0QL-4

### IMPORTS
import streamlit as st
from rasa.core.agent import Agent
import asyncio

from weather_information import WeatherInformation
from viz_dash import VisualizationDashboard
from chatbotUI import ChatbotUI


class ChatbotController:
    def __init__(self, model_path="./models/20231218-082112-open-edging.tar.gz"):
        """initialize the chatbot framework"""
        self.agent = Agent.load(model_path)
        print(f"Model: {self.agent}")
        self.responses = dict()
        st.title("Weather Chatbot")

        with st.chat_message(name="assistant"):
            st.markdown("Hey I am your AI based assistant")

        # Setting up the session state with a loop that shows the conversation
        # In the chat message I can add my own avatar if I want
        if "messages" not in st.session_state:
            st.session_state.messages = []


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
            self.get_user_input(prompt=prompt)
            asyncio.run(self.get_chatbot_response(prompt=prompt))
        
        # At the end of the answers print the visualization dashboard
        wi = WeatherInformation(self.responses)
        wi.get_weather_info()

        vd = VisualizationDashboard(wi)
        plots = vd.run()

        chat_UI = ChatbotUI(plots, wi["location"], wi['days'])
        chat_UI.display_plots()


