import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
birddata = pd.read_csv("bird_tracking.csv", index_col=0)

#Exercise 1


# First, use `groupby()` to group the data by "bird_name".
grouped_birds = birddata.groupby('bird_name')

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds['speed_2d'].mean()

# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds['altitude'].mean()

#Exercise 2

# Convert birddata.date_time to the `pd.datetime` format.
birddata.date_time = pd.to_datetime(birddata.date_time)

# Create a new column of day of observation
birddata["date"] = birddata['date_time'].dt.date

# Use `groupby()` to group the data by date.
grouped_bydates = birddata.groupby("date",group_keys=True)

# Find the mean `altitude` for each date.
mean_altitudes_perday = grouped_bydates["altitude"].mean()

date = datetime.strptime("2013-09-12", "%Y-%m-%d").date()

print(mean_altitudes_perday[date])

#Exercise 3

# Use `groupby()` to group the data by bird and date.
grouped_birdday = birddata.groupby(['bird_name','date'])

# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = grouped_birdday["altitude"].mean()

name = "Eric"
date = datetime.strptime("2013-08-18", "%Y-%m-%d").date()

print(mean_altitudes_perday[name,date])

#Exercise 4

import matplotlib.pyplot as plt


speed_2d = grouped_birdday["speed_2d"].mean()
eric_daily_speed  = speed_2d["Eric"]
sanne_daily_speed = speed_2d["Sanne"]
nico_daily_speed  = speed_2d["Nico"]


eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()
















