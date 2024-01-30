# streamlit run __main__.py
from controller import ChatbotController

if __name__ == "__main__":
    # Initialize and run the Chatbot Controller
    chatbot = ChatbotController()
    chatbot.run()