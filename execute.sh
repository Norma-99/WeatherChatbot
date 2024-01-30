#!/bin/bash

# Get the current directory
current_directory=$(pwd)

# Open the first terminal, change to the current directory, and execute 'rasa run actions'
osascript -e "tell application \"Terminal\" to do script \"cd '$current_directory'; rasa run actions\""

# Open the second terminal, change to the current directory, and execute 'rasa shell --debug'
osascript -e "tell application \"Terminal\" to do script \"cd '$current_directory'; rasa shell --debug\""

# Open the third terminal, change to the current directory, and execute 'streamlit run __main__.py'
osascript -e "tell application \"Terminal\" to do script \"cd '$current_directory'; streamlit run __main__.py\""
