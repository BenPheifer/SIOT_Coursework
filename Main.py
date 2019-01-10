#!/usr/bin/python2
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from weather_retrieve import weather
from distance_retrieve_method2 import duration
from datetime import datetime
from runHTML import htmlwrite
import time
import webbrowser

keys = json.load(open('keys.json'))  # json location of authorisation keys

# Authorise Google Api
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
google_cred = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(google_cred)

sheet = gc.open("SIOTData").sheet1  # Opens Spreadsheet in gDrive


# Location Latitudes and Longitudes
London = ("51.5074", "0.1278")
Bayside = ('53.3796218', '-6.17306')
Home = ('53.3585869', '-6.1788813')
School = ('53.3769649', '-6.0960984')
Galway = ('53.2707676', '-9.057223')
UCD = ('53.308201', '-6.2322493')
Work = ('53.3495159','-6.256905')

Browser_open = False

destinations = [School, Work, UCD, Galway]  # selection of destinations to measure from home startpoint

# Continuously run code
while True:
    time_updated = False  # reset
    try:
        try:
            times = []
            for i in range(0, len(destinations)):  # iterate through destinations
                print i
                times.append(duration(keys["gmaps_key"], Home, destinations[i]))  # Calls function from distance_retrieve.py
            print "google_map_data_retrieved"
            time_updated = True  # Boolean to ascertain new data has been collected
        except:
            print ("cannot_retrieve_google_map_data")
            pass
        try:
            package = weather(keys["dark_sky_key"], Bayside, convert_unix=True)  # Calls function from weather_retrieve.py
            print "weather_data_retrieved"

        except:
            t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            package = [t, '', '', '']  # Give empty cells if data retrieval fails
            print ("cannot_retrieve_weather_data")
            pass

        if time_updated:  # Avoid repeated data points if retrieval fails
            package += times  # concatenate lists
        else:
            for i in range(0, len(times)):
                package += ['']  # Give empty cells for failed data collection
        print datetime.now()

        try:
            sheet.append_row(package)  # send package to spreadsheet
            print "data_posted"

        except:
            print ("data_upload_failed")
            # Authorise Google Api
            scope = ['https://spreadsheets.google.com/feeds',
                     'https://www.googleapis.com/auth/drive']
            google_cred = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
            gc = gspread.authorize(google_cred)

            sheet = gc.open("SIOTData").sheet1  # Opens Spreadsheet in gDrive

            pass
        htmlwrite("new.html", times[0], times[1], times[2], times[3])
        print times[0]
        if not Browser_open:
            webbrowser.open_new_tab("new.html")
            Browser_open = True
        time.sleep(5)  # Sample data every minute

    except KeyboardInterrupt:
        break
