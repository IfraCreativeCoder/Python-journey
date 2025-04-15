# The Date and Time.

# What is Epoch Time?
# Epoch time,is a system for tracking time that counts the number of seconds,
# which is defined as 00:00:00 UTC on January 1, 1970.It is widely used in
# computing and programming to represent time in a standardized format.

# Epoch used in python.
# time.time() , time.gmtime(seconds) , time.localtime(seconds).

import time
tricks = time.time()
print("Number of tricks since 12:00am, january 1, 1970:", tricks)

# Current time.
import time
localtime = time.localtime(time.time())
print("Current local time is:", localtime)

# Formatted time "get time in readable format".
import time 
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

#The Calendar
import calendar
cal = calendar.month(2025, 1)
print("Here is the calendar:")
print(cal) 

# The Date Time
from datetime import date
date1 = date(2023, 4, 19)
print("Date:", date1)

date2 = date(2023, 4, 30)
print("Date:", date2)

import datetime
x = datetime.datetime.now()
print(x)

# The strftime() methode, formating date object into readable strings.
import datetime
x = datetime.datetime(2025, 1, 1)
print(x.strftime("%f")) # Weekday, full name.
print(x.strftime("%A")) # day
print(x.strftime("%Y")) # year
print(x.strftime("%B")) # Month, full name.



