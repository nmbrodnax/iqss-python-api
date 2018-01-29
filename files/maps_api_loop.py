# maps_api_loop.py
# Introduction to Using APIs with Python
# NaLette Brodnax
# www.nalettebrodnax.com

import csv
import json
import requests

# REVIEW
# ============================
host = 'https://maps.googleapis.com/maps/api/geocode/json'


# ACCESS - PARSE - TRANSFORM
# ============================
local_file = 'google_auth.txt'
with open(local_file) as txtfile:
    my_key = txtfile.read()
    # print("API Key: " + my_key)

def get_coordinates(address, api_key):
    """Returns a list with latitude and longitude for a given address
    str, str -> list"""
    url = host + "?address=" + address + "&key=" + api_key
    response = requests.request('GET', url)
    geo = response.json()
    results = geo['results'][0]
    # return a list 
    return [results['geometry']['location']['lat'],\
            results['geometry']['location']['lng']]


# STORE
# ============================
# identify the fieldnames in a csv file
csvfile = open("charter_schools.csv", 'r')
header = csvfile.readline()
csvfile.close()

# print(header) # a string with newline and commas
header = header.strip('\n') # remove the new line character
fieldnames = header.split(',') # split string at each tab character

# get coordinates for list of addresses
with open("charter_schools.csv", "r") as infile, \
     open("charter_schools_geo.csv", "w") as outfile:

    # create a reader object to read rows from your infile
    reader = csv.DictReader(infile, fieldnames)
    next(reader, None) # skip over the header row

    # create a writer object to add rows to your outfile
    fieldnames.append('LATITUDE') # name for new column
    fieldnames.append('LONGITUDE') # name for new column
    writer = csv.DictWriter(outfile, fieldnames)
    writer.writeheader()

    # get school from infile, add coordinates, save school info to outfile
    for school in reader:
        school_address = school['ADDRESS'] + ", " + school['CITY STATE ZIP']
        location = get_coordinates(school_address, my_key)
        school['LATITUDE'] = location[0]
        school['LONGITUDE'] = location[1]
        writer.writerow(school)

