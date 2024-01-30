# WeatherChatbot
This is a simple weather chatbot created using Rasa and Streamlit libraries from Python


For the training I typed: 
```rasa init --no-promp``` so it created all the necessary files for training (maybe later I will take out some of them)


https://medium.com/analytics-vidhya/building-a-simple-weather-chatbot-using-rasa-54eaf97daa82

Rasa video: 
- https://www.youtube.com/watch?v=suZvPjnSHA0

## Installations

```pip3 install rasa```
```pip3 install streamlit```


## Commands: 
```rasa shell --debug```

```streamlit run __main__.py```

```rasa train```

## To run the pipeline:
Open 3 terminals and then execute in each terminal one of these commands (one for each terminal):
```rasa run actions```

```rasa shell --debug```

```streamlit run __main__.py```

Another alternative is to run the `execute.sh` file. 
To do so, first give the script execute permissions: `chmod +x execute.sh`
Then execute the file `./execute.sh`