## This file contains the majority of the backend logic of the chatbot.
import streamlit as st
import requests
import ast

from weather_information import WeatherInformation
from viz_dash import VisualizationDashboard
from chatbotUI import ChatbotUI


class ChatbotController:
    def __init__(self, endpoint_url:str = "http://0.0.0.0:5005/webhooks/rest/webhook"):
        """
        Initialize the ChatbotController instance.
        
        Args:
        endpoint_url (str): The URL of the chatbot backend service.

        This constructor sets up the chatbot interface, including initializing the Streamlit UI,
        setting the chatbot endpoint, and preparing the session state to store conversation messages.
        """
        self.endpoint_url = endpoint_url
        print(f"Endpoint: {self.endpoint_url}")
        self.responses = dict()
        st.title("Weather Chatbot")

        # Initial chat message from the assistant.
        with st.chat_message(name="assistant"):
            st.markdown("Hey I am your AI based assistant")

        # Initialize a session state for storing chat messages if it doesn't exist.
        if "messages" not in st.session_state:
            st.session_state.messages = []
    

    def process_interaction(self, prompt):
        """
        Process user interaction with the chatbot.

        Args:
        prompt (str): The user's input message.

        This function sends the user's input to the chatbot service, receives the response,
        and updates the Streamlit UI with both the user's message and the chatbot's response.
        """
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user's message in the chat.
        with st.chat_message("user"):
            st.markdown(prompt)

        body_json = {
            'sender': 'streamlit',
            'message': prompt
        }

        # Make a POST request to the chatbot backend and get the response.
        post_response = requests.post(self.endpoint_url, json=body_json)
        post_response_json = post_response.json()
        print(post_response_json)

        # Process the response from the chatbot.
        if post_response: 
            bot_response = [elem['text'] for elem in post_response_json]
        
        # Display chatbot's responses in the chat.
        with st.chat_message("assistant"):
            for response in bot_response:
                if response.startswith("[ACTION SERVER]"):
                    self.update_responses(response=response)
                else: 
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.markdown(response)


    def update_responses(self, response: str) -> None:
        """
        Update the responses dictionary based on the chatbot's response.

        Args:
        response (str): The chatbot's response message.

        This function extracts and processes special action server responses from the chatbot,
        updates the internal responses dictionary, and triggers visualization dashboard generation.
        """
        try: 
            splits = response.split(']')
            split = splits[1]
            json_response = ast.literal_eval(split.replace("'", "\""))
            self.responses = json_response
        except: 
            raise Exception(f"The response message is not in the correct format. Response: {response}")
        self.get_final_visualization_dashboard()



    def get_final_visualization_dashboard(self):
        """
        Generate and display the final visualization dashboard based on the chatbot responses.

        This function creates a WeatherInformation instance, retrieves weather information,
        prepares visualization plots, and displays them using ChatbotUI.
        """
        wi = WeatherInformation(self.responses)
        info = wi.get_weather_info()

        print(info)
        vd = VisualizationDashboard(info)
        plots = vd.run()

        chat_UI = ChatbotUI(plots, info["location"], info['days'])
        chat_UI.display_plots()


    def run(self):
        """
        Run the chatbot UI in the Streamlit application.

        This function is responsible for displaying the entire conversation history in the chat
        and handling new user inputs through the chat interface.
        """
        # Display all previous messages in the conversation.
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Handle new user input.
        if prompt := st.chat_input("Type your query"):
            self.process_interaction(prompt=prompt)
