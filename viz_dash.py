import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime



class VisualizationDashboard:
    def __init__(self, viz_info: dict):
        # Create a DataFrame
        self.viz_info = viz_info
        self.df = pd.DataFrame({
            'Date': viz_info['days_list'],
            'Temperature': viz_info['temperature'],
            'Precipitation': viz_info['precipitation'],
            'Wind': viz_info['wind'],
            'Humidity': viz_info['humidity']
        })
        # Set Date as the index
        self.df['Date'] = pd.to_datetime(self.df['Date'], format='%m/%d/%y')
        self.df.set_index('Date', inplace=True)
        self.plots = dict()


    def create_plot(self, df_index: str, metric: str):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(self.df.index, self.df[df_index], marker='o', label=df_index)
        ax.set_title(f'{df_index} Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel(f'{df_index} ({metric})')
        ax.legend()
        return fig


    def get_temperature_plot(self):
        # Temperature plot
        self.plots['temperature'] = self.create_plot(df_index='Temperature', metric='°C')


    def get_precipitation_plot(self):
        # Precipitation plot
        # This is a bar plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(self.df.index, self.df['Precipitation'], label='Precipitation')
        ax.set_title('Precipitation Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Precipitation (mm)')
        ax.legend()
        self.plots['precipitation'] = fig


    def get_wind_plot(self):
        # Wind plot
        self.plots['wind'] = self.create_plot(df_index='Wind', metric='m/s')


    def get_humidity_plot(self):
        # Humidity plot
        self.plots['humidity'] = self.create_plot(df_index='Humidity', metric='%')


    def get_sunrise_sunset_plot(self):
        # Extracting sunrise and sunset data
        sunrise_times, sunset_times = zip(*self.viz_info['sunrise_sunset'])

        # Converting time strings to datetime objects
        sunrise_times = [datetime.strptime(time, '%I:%M%p') for time in sunrise_times]
        sunset_times = [datetime.strptime(time, '%I:%M%p') for time in sunset_times]

        # Extracting hours from datetime objects
        sunrise_hours = [time.hour + time.minute / 60 for time in sunrise_times]
        sunset_hours = [time.hour + time.minute / 60 for time in sunset_times]

        # Plotting the data
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(self.viz_info['days_list'], sunrise_hours, label='Sunrise', marker='o')
        ax.plot(self.viz_info['days_list'], sunset_hours, label='Sunset', marker='o')

        # Formatting the x-axis ticks for better readability
        ax.set_xticks(self.viz_info['days_list'])
        ax.tick_params(axis='x', rotation=45)

        # Formatting the y-axis ticks with time in the format '8:00AM', '10:00AM', etc.
        y_ticks = range(0, 24, 2)
        ax.set_yticks(y_ticks)
        ax.set_yticklabels([datetime.strptime(str(int(hour)) + ':00', '%H:%M').strftime('%I:%M%p') for hour in y_ticks])

        # Adding labels and title
        ax.set_xlabel('Date')
        ax.set_ylabel('Time')
        ax.set_title('Sunrise and Sunset Data')

        # Adding a legend
        ax.legend()

        # Displaying the exact time on each data point
        for i, date in enumerate(self.viz_info['days_list']):
            ax.text(date, sunrise_hours[i], sunrise_times[i].strftime('%I:%M%p'), ha='center', va='bottom')
            ax.text(date, sunset_hours[i], sunset_times[i].strftime('%I:%M%p'), ha='center', va='top')

        # Displaying the plot
        fig.tight_layout()
        self.plots['sunrise_sunset'] = fig


    def run(self):
        self.get_temperature_plot()
        self.get_precipitation_plot()
        self.get_wind_plot()
        self.get_humidity_plot()
        self.get_sunrise_sunset_plot()

        # plt.show()
        return self.plots



sample_data = {
    'location': 'london', 
    'days': 4, 
    'temperature': [6, 5, 18, 29], 
    'precipitation': [8.90413883114445, 0.33233459627986184, 4.3122270213482015, 8.500102619951065], 
    'wind': [14.834515085743334, 6.6653584874527505, 7.305588651356283, 13.370943297023864], 
    'humidity': [22, 80, 35, 5], 
    'sunrise_sunset': [('08:22AM', '08:52PM'), ('08:06AM', '06:38PM'), ('07:58AM', '07:42PM'), ('08:39AM', '07:07PM')], 
    'days_list': ['01/09/24', '01/10/24', '01/11/24', '01/12/24']
}

vd = VisualizationDashboard(sample_data)
plots = vd.run()
