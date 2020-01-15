#!/usr/bin/env python
# coding: utf-8

# # WeatherPy
# ----
# 
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time

# Import API key
from api_keys import api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# In[ ]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
city.head()


# ### Perform API Calls
# * Perform a weather check on each city using a series of successive API calls.
# * Include a print log of each city as it'sbeing processed (with the city number and city name).
# 

# In[23]:


base_url = "http://api.openweathermap.org/data/2.5/weather?"
units = "imperial"

query_url = f"{base_url}appid={api_key}&units={units}&q="

lat = []
temp = []
humidity = []
all = []
speed = []

for city in cities:
    response = requests.get(query_url + city).json()
    lat.append(response['coord']['lat'])
    temp.append(response['main']['temp'])
    humidity.append(response['main']['humidity'])
    all.append(response['clouds']['all'])
    speed.append(response['wind']['speed'])


# ### Convert Raw Data to DataFrame
# * Export the city data into a .csv.
# * Display the DataFrame

# In[4]:


data = [response(*summary) for response in weather_data]


weather_data = pd.DataFrame(data, index=cities)
weather_data.value_counts()


# In[5]:


weather_data.head()


# ### Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# #### Latitude vs. Temperature Plot

# In[6]:


plt.scatter(lat, temp, marker="o", facecolors="blue", edgecolors="black")


# #### Latitude vs. Humidity Plot

# In[7]:


plt.scatter(lat, humidity, marker="o", facecolors="blue", edgecolors="black")


# #### Latitude vs. Cloudiness Plot

# In[8]:


plt.scatter(lat, all, marker="o", facecolors="blue", edgecolors="black")


# #### Latitude vs. Wind Speed Plot

# In[9]:


plt.scatter(lat, speed, marker="o", facecolors="blue", edgecolors="black")


# In[ ]:




