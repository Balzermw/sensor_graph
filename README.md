The main purpose of this program to grab and display temperature data from a Samsara environment monitor (EM21,EM22).

Please edit the settings.py to add the widget ID from your EM sensor. You can find the widget ID for any sensor by selecting it from the Samsara Dashboard. The widget ID is at the end of the URL when viewing a temperature sensor. 

For example:
https://cloud.samsara.com/o/6081/widgets/**********/show


The groupID and API token can be found in the settings page on your org in the API Tokens section. If you don’t already have an API token you’ll need to create one.

The temperature_end_point and api_time_format should not need to be edited. 


Features:

- Live temperature graph (~3 minutes between data update)
- Modular design allows user to add different sensor to graph through settings.py
- Adjust how often to graph data (interval parameter in main.py)
- Adjust how many total data points to display (graph_points parameter in main.py)

Quick Start on Mac:

1. Install libraries (Matplotlib, JSON, requests through pip or otherwise) 
2. Open terminal window. Type “python3 ” then drag the main.py file into the terminal window. Hit enter to start.

For example:
Michaels-MacBook-Pro-4:~ michaelbalzer$ python3 /Users/michaelbalzer/GraphTempProgram/main.py 

