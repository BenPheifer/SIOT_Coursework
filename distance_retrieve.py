#!/usr/bin/python2
import json
from requests import get


def duration(key, start, end):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins={},{}&destinations={},{}&key={}'\
        .format(start[0], start[1], end[0], end[1], key)

    distance = get(url)
    distance_dic = json.loads(distance.content)
    # print type(distance_dic)
    # print distance_dic
    data = distance_dic[u'rows'][0][u'elements'][0]  # Pulling out desired information
    # print type(data)
    # print data

    travel_time = data[u'duration'][u'value']

    return travel_time

