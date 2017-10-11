# maps_api.py
# Introduction to Using APIs with Python
# Harvard IQSS
# October 13, 2017

# NaLette Brodnax
# nbrodnax@iq.harvard.edu
# www.nalettebrodnax.com

import csv
import json
import requests


# REVIEW
# ============================
# go to https://developers.google.com/maps/documentation/geocoding/start
# identify location and format of api
host = 'https://maps.googleapis.com/maps/api/geocode/json'


# ACCESS
# ============================
# get authentication parameters from local file
local_file = 'google_auth.txt'
with open(local_file) as txtfile:
    my_key = txtfile.read()
    # print("API Key: " + my_key)

# build api GET request
address = "1737 Cambridge St, Cambridge, MA 02138" 
url = host + "?address=" + address + "&key=" + my_key

# check the HTTP response code
response = requests.request('GET', url)
print(response)


# PARSE
# ============================
# parse the JSON data into a python dictionary
geo = response.json()


# TRANSFORM
# ============================
# display the result in an easy-to-read format
print(json.dumps(geo, indent = 4, sort_keys = True))

# examine structure
print(type(geo)) # geo is a dictionary
print(geo.keys()) # check the dictionary keys
results = geo['results'][0] 
print(results.keys())


# STORE
# ============================
# save the relevant data
longitude = results['geometry']['location']['lng']
latitude = results['geometry']['location']['lat']
