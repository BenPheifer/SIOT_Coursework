#!/usr/bin/python2
from datetime import datetime
import googlemaps


def duration(key, start, end):
    now = datetime.now()
    maps = googlemaps.Client(key=key)

    directions_result = maps.directions(start,  # Call Directions from Google Maps, start latitude and longitude
                                        end,  # end latitude and longitude
                                        mode="driving",  # driving mode
                                        departure_time=now  # set departure time to now for live traffic updates
                                        )
    time = directions_result[0]['legs'][0]['duration_in_traffic']  # extract travel time from

    return time['value']

