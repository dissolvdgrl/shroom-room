'''
    Main script to control the Raspberry Pi temperature
    and humidity sensor.

    This requires a MongoDB database to be running.
    Please see the README for hardware details.
'''

# get mongoDB Atlas connection
from db import get_database

temp_database = get_database('temperature')
humidity_database = get_database('humidity')

# How do I want to structure this data?
'''
    {
        "date": "",
        "time": "",
        temperature: ""
    }
    
    {
        "date": "",
        "time": "",
        "humidity": ""
    }
    
    Collection interval of once per hour, perhaps.
'''
