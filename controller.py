### HELPFUL INFORMATION
#   HELPFUL VIDEO: https://www.youtube.com/watch?v=skKNjq0QL-4

### IMPORTS
import streamlit as st


class ChatbotController:
    def __init__(self):
        """initialize the chatbot framework"""
        self.responses = dict()
        st.title("Weather Chatbot")
        with st.chat_message(name="assistant"):
            st.markdown("Hey I am your AI based assistant, what can I help you with?")

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


    def get_chatbot_response(self, prompt:str) -> None:
        with st.chat_message("assistant"):
                ### DO HERE THE CHATBOT LOGIC
                st.session_state.messages.append({"role": "assistant", "content": prompt})
                self.update_responses(user_input=prompt, response=prompt)
                st.markdown(prompt)


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
            self.get_chatbot_response(prompt=prompt)