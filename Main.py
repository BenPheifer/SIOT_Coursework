#!/usr/bin/python2
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from weather_retrieve import weather
from distance_retrieve import duration
import time

keys = json.load(open('keys.json'))

print keys["dark_sky_key"]
# Authorise Google Api

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
google_cred = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(google_cred)

sheet = gc.open("SIOTData").sheet1

London = ("51.5074", "0.1278")  # Lattitude and Longtitude for London
Bayside = ('53.3796218', '-6.17306')  # Midway point on Journey
Home = ('53.3585869', '-6.1788813')
School = ('53.3769649', '-6.0960984')


try:
    duration_seconds = duration(keys["gmaps_key"], Home, School)
    print "Google-Map Data Retrieved"
except:
    raise Exception("Cannot Retrieve Duration Data")

try:
    package = weather(keys["dark_sky_key"], Bayside, convert_unix=True)
    print "weather-data retrieved"
except:
    raise Exception("Cannot Retrieve Weather Data")

package.append(duration_seconds)
while True:
    sheet.append_row(package)
    print "Data Posted"
    time.sleep(30)

