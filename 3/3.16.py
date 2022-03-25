# Manipulating Dates Involving Time Zones
# 3.16.1
from datetime import datetime, timedelta
from pytz import timezone
d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

# Localize the date for chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# 3.16.2
# Convert to Banglore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

# 3.16.3
d = datetime(2012, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)

# 3.16.4
from datetime import timedelta
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

# Discussion
print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)

# --
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

pytz.country_timezone['IN']