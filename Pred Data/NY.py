#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:01:39 2022

@author: salvadorsanchez
"""

from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='user_agent')

locator = Nominatim(user_agent='myGeocoder')


df = pd.read_csv('/Users/salvadorsanchez/Dropbox/ADS/ADS 505 Applied Data Sci for Business/Tableau/police-settlements/new_york_ny/final/new_york_edited.csv')

#df = df.head(25)


# 1 - conveneint function to delay between geocoding calls
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
# 2- - create location column
df['location_geo'] = df['location'].apply(geocode)
# 3 - create longitude, laatitude and altitude from location column (returns tuple)
df['point'] = df['location_geo'].apply(lambda loc: tuple(loc.point) if loc else (0, 0, 0))
# 4 - split point column into latitude, longitude and altitude columns
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(),
                                                         index=df.index
                                                         )

df.to_csv('NY.csv')