'''
Start to Code
=============
Workshop: Web of Things (IoT)
Application: Ambilight
--------------------------------------
Author: Philippe De Pauw - Waterschoot
Opleiding: Grafische en digitale media
Specialisatie: New Media Development
'''

# Import the necessary libraries
from sense_hat import SenseHat
from time import sleep
import sys
import os
from google.cloud import firestore

# Constants


# Make an instance of SenseHat

# Initalize Firebase
# Use the service account for own server

# function: convertHexValueToTuple(hex_value)
def convertHexValueToTuple(hex_value):
    r = int(hex_value[1:3], 16)
    g = int(hex_value[3:5], 16)
    b = int(hex_value[5:], 16)
    return (r, g, b)

# Endless loop
while True:
    try:
        pass

    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
        sys.exit(0)