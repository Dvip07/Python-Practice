# Converting Strings into Datetimes
# 3.15.1
from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
diff

# Discussion
z
nice_z = datetime.strftime(z, '%A %B %d %Y')
nice_z

