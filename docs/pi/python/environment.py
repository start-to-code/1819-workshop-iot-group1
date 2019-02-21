'''
Start to Code
=============
Workshop: Web of Things (IoT)
Application: Environment Sensors
--------------------------------------
Author: Philippe De Pauw - Waterschoot
Opleiding: Grafische en digitale media
Specialisatie: New Media Development
'''

# Import the necessary libraries
from sense_hat import SenseHat
from time import sleep
from datetime import datetime
import sys
import os
from google.cloud import firestore

# Constants

# Variables

# Make an instance of SenseHat

# Initalize Firebase
# Use the service account for own server

# function: get_real_temp()
# get the real temperature
def get_real_temp():
    res = os.popen('python3 temperature_real.py False').readline()
    t = float(res.replace('temp=', '').replace("C\n", ''))
    return(t)

while True:
    try:        
        pass
        
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
        sys.exit(0)