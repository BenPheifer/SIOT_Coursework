#!/usr/bin/python2
import json
from datetime import datetime
from requests import get


def weather(key, location, cloud_percent=False, convert_unix=True, fahrenheit=False):
    requester = "https://api.darksky.net/forecast/{}/{loc[0]:},{loc[1]:}?/units=[si]".format(key, loc=location)
    current_weather = get(requester)
    weather_dic = json.loads(current_weather.text)['currently']
    weather_list = [weather_dic[u'time'], weather_dic[u'cloudCover'], weather_dic[u'apparentTemperature'],
                    weather_dic[u'precipIntensity']]  # Selected Relevant Weather Attributes

    if cloud_percent:  # Convert cloud cover to percentage
        weather_list[1] *= 100

    if not fahrenheit:  # Convert apparent temperature Fahrenheit to Celsius
        weather_list[2] = (weather_list[2] - 32)*5/9

    if convert_unix:  # Convert time data from unix to understandable date and time
        unix_time = weather_list[0]
        time_date = datetime.fromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')
        weather_list[0] = time_date

    return weather_list

