import time
from datetime import datetime

# show current time in unix timestamp or epoch format
print(time.time())

# Create a date time object
dt = datetime(2022, 1, 1)

# Get current date time
print(datetime.now())

# Convert a string representation of datetime to datetime object
# we use the directives to specific the different components of a datetime i.e year, month etc
dt = datetime.strptime("2002/11/12", "%Y/%m/%d")
print(dt)

# convert datetime object to string
print(datetime(2003, 8, 12, 13, 34, 12).strftime("%Y-%m%dT%H:%M:%S"))

event_date = datetime(1472, 7, 12)

current_date = datetime.now()

delta = current_date - event_date

print("Delta:", delta)

print(f"Delta in Days: {delta.days}")

# seconds represent the delta hours in seconds, basically the hours next to days
print(f"Delta seconds: {delta.seconds}")

# total_seconds() return the delta in seconds
print("Delta in seconds", delta.total_seconds())