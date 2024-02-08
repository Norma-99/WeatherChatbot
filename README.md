# WeatherChatbot

This is a simple weather chatbot created using Rasa and Streamlit libraries from Python

To enable rasa the first time I downloaded it and typed: ```rasa init --no-promp``` so it created all the necessary files for training.


## Installations

Install Python: https://www.python.org/downloads/release/python-390/

To execute the code first there are some libraries that should be installed.

```pip3 install rasa```

```pip3 install streamlit```

```pip3 install matplotlib```

```pip3 install seaborn```

```pip3 install spacy```

```pip3 install word2number```


## To run the pipeline 

To execute the code there are 2 options. 

### Option 1

Open 3 terminals and then execute in each terminal one of these commands (one for each terminal):

```rasa run actions```

```rasa shell --debug```

```streamlit run __main__.py```

### Option 2

Another alternative is to run the `execute.sh` file. 

To do so, first give the script execute permissions: `chmod +x execute.sh`

Then execute the file `./execute.sh` and wait for 30 seconds so it all initializes. 