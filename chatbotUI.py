import streamlit as st


class ChatbotUI:
    def __init__(self, plots: dict, location: str, days: str):
        """
        Initialize the ChatbotUI instance.

        Args:
        plots (dict): A dictionary where keys are plot names and values are plot objects.
        location (str): The location for which the weather information is relevant.
        days (str): The number of days for which the weather information is being displayed.
        """
        self.plots = plots
        self.days = days
        self.location = location

        # Display the title of the dashboard in the Streamlit UI
        st.title("Weather Dashboard")


    def display_plots(self):
        """
        Display each plot in the Streamlit UI.

        Iterates through the keys in the `plots` dictionary and displays each plot
        followed by a descriptive text about the plot.
        """
        for plot_name in list(self.plots.keys()):
            st.pyplot(self.plots[plot_name])
            st.text(f"{plot_name} plot for the next {self.days} days in {self.location}.")