import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import seaborn as sns

# Set a seaborn style for better aesthetics
sns.set(style="whitegrid")


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


    def get_temperature_plot(self):
        # Temperature plot
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Smoothed line plot
        sns.lineplot(x=self.df.index, y=self.df['Temperature'], palette="Blues_d", ax=ax, ci=None, marker='o')
        
        # Overlay individual data points with temperature labels
        sns.scatterplot(x=self.df.index, y=self.df['Temperature'], color='blue', ax=ax, label='Data Points')
        for i, temp in enumerate(self.df['Temperature']):
            ax.text(self.df.index[i], temp, f'{temp} °C', ha='right', va='bottom', fontsize=10)

        ax.set_title(f'Temperature Over Time', fontsize=14, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel(f'Temperature (°C)', fontsize=12)
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        ax.legend(loc='best')
        self.plots['temperature'] = fig


    def get_precipitation_plot(self):
        # Precipitation plot
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=self.df.index, y=self.df['Precipitation'], palette="Blues_d", ax=ax)
        # Add text labels for precipitation values on top of each bar
        for i, val in enumerate(self.df['Precipitation']):
            ax.text(i, val, f'{val:.2f} mm', ha='center', va='bottom', fontsize=10)
        ax.set_title(f'Precipitation Over Time', fontsize=14, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel(f'Precipitation (mm)', fontsize=12)
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        self.plots['precipitation'] = fig


    def get_wind_plot(self):
        # Wind plot
        fig, ax = plt.subplots(figsize=(10, 6))

        sns.lineplot(x=self.df.index, y=self.df['Wind'], palette="PuBuGn_d", ax=ax, ci=None, marker='o')

        # Overlay individual data points
        sns.scatterplot(x=self.df.index, y=self.df['Wind'], color='blue', ax=ax, label='Data Points')
        for i, wind in enumerate(self.df['Wind']):
            ax.text(self.df.index[i], wind, f'{round(wind,2)} m/s', ha='left', va='bottom', fontsize=10)

        ax.set_title(f'Wind Speed Over Time', fontsize=14, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel(f'Wind (m/s)', fontsize=12)
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        self.plots['wind'] = fig


    def get_humidity_plot(self):
        # Humidity plot
        fig, ax = plt.subplots(figsize=(10, 6))

        sns.lineplot(x=self.df.index, y=self.df['Humidity'], palette="PuBuGn_d", ax=ax, ci=None, marker='o')

        # Overlay individual data points
        sns.scatterplot(x=self.df.index, y=self.df['Humidity'], color='blue', ax=ax, label='Data Points')
        for i, hum in enumerate(self.df['Humidity']):
            ax.text(self.df.index[i], hum, f'{hum} m/s', ha='right', va='bottom', fontsize=10)

        ax.set_title(f'Humidity Over Time', fontsize=14, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel(f'Humidity (%)', fontsize=12)
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        self.plots['humidity'] = fig


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
        ax.plot(self.viz_info['days_list'], sunrise_hours, label='Sunrise', marker='o', color='orange')
        ax.plot(self.viz_info['days_list'], sunset_hours, label='Sunset', marker='o', color='purple')

        # Formatting the x-axis ticks for better readability
        ax.set_xticks(self.viz_info['days_list'])
        ax.tick_params(axis='x', rotation=45)

        # Formatting the y-axis ticks with time in the format '8:00AM', '10:00AM', etc.
        y_ticks = range(0, 24, 2)
        ax.set_yticks(y_ticks)
        ax.set_yticklabels([datetime.strptime(str(int(hour)) + ':00', '%H:%M').strftime('%I:%M%p') for hour in y_ticks])

        # Adding labels and title
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Time', fontsize=12)
        ax.set_title('Sunrise and Sunset Times', fontsize=14, fontweight='bold')
        
        # Adding a legend
        ax.legend()

        # Displaying the exact time on each data point
        for i, date in enumerate(self.viz_info['days_list']):
            ax.text(date, sunrise_hours[i], sunrise_times[i].strftime('%I:%M%p'), ha='center', va='top', fontsize=8)
            ax.text(date, sunset_hours[i], sunset_times[i].strftime('%I:%M%p'), ha='center', va='top', fontsize=8)

        # Displaying the plot
        fig.tight_layout()
        self.plots['sunrise_sunset'] = fig


    def run(self):
        plot_convertor = {
            "temperature": self.get_temperature_plot,
            "precipitation": self.get_precipitation_plot,
            "wind": self.get_wind_plot,
            "humidity": self.get_humidity_plot,
            "sunrise_sunset": self.get_sunrise_sunset_plot
        }
        for key in self.viz_info:
            if (self.viz_info[key] is not None) and (key in list(plot_convertor.keys())):
                plot_convertor[key]()
        return self.plots



sample_data = {
    'location': 'london', 
    'days': 4, 
    'temperature': [6, 5, 18, 29], 
    # 'precipitation': [8.90413883114445, 0.33233459627986184, 4.3122270213482015, 8.500102619951065], 
    # 'wind': [14.834515085743334, 6.6653584874527505, 7.305588651356283, 13.370943297023864], 
    # 'humidity': [22, 80, 35, 5], 
    # 'sunrise_sunset': [('08:22AM', '08:52PM'), ('08:06AM', '06:38PM'), ('07:58AM', '07:42PM'), ('08:39AM', '07:07PM')], 
    'days_list': ['01/09/24', '01/10/24', '01/11/24', '01/12/24']
}

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
