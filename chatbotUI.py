import streamlit as st


class ChatbotUI:
    def __init__(self, plots: dict, days: str, location: str):
        """Initialize the chatbot UI"""
        self.plots = plots
        self.days = days
        self.location = location
        st.title("Weather Dashboard")


    def display_plots(self):
        for plot_name in list(self.plots.keys()):
            st.pyplot(self.plots[plot_name])
            st.text(f"{plot_name} plot for the next {self.days} days in {self.location}.")

    # def UI_design():
    #     """This function contains all the frontend design"""
    #     pass

    # def background_design():
    #     pass

    # def dialog_design():
    #     pass
