# time → works with timestamps & delays
# datetime → works with date + time together
# date → part of datetime module
# Used for:
# current time
# date operations
# formatting
import datetime as dt

# print(dt.datetime.now());#get current date and time
# print(dt.datetime(2026,7,31,12,25,8))#2026-07-31 12:25:08

#formating
# strftime() → format date/time into string
# Converts datetime → string
# Uses format codes (%Y, %m, etc.)
# Belongs to datetime module
# %b   # Short month name (Jan, Feb)
# %B   # Full month name (January)
# %m   # Month number (01–12)
# %y   # Year (2 digits → 26)
# %Y   # Year (4 digits → 2026)
# %H   # Hour (24-hour format → 00–23)
# %I   # Hour (12-hour format → 01–12)
# %p   # AM / PM
# %M   # Minute (00–59)
x=dt.datetime.now();
print(x.strftime("%Y"))
print(x.strftime("%p"))
print(x.strftime("%m"))
print(x.strftime("%M"))
print(x.strftime("%I"))
