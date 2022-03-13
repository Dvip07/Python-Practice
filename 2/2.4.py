# Matching and Searching for Text Patterns
# 2.4.1

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact Match
text == 'yeah'

# Match at start or end
text.startswith('yeah')
text.endswith('no')

# Search for the location of the firsr occurence
text.find('no')


# 2.4.2
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')


# 2.4.3
datepat = re.compile('r\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

# 2.4.4
text = 'Today is 11/27/2012. Pycon starts 3/13/2013.'
datepat.findall(text)

# --
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')


# 2.4.5
m = datepat.match('11/27/2012')
m

# Extract the contents of each group
m.group(0)
m.group(1)
m.group(2)
m.group(3)
m.groups()
month, day, year = m.groups()

# Find all matches (notice splitting into tuples)
text
datepat.findall(text)
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year,month,day))


# 2.4.6
for m in datepat.finditer(text):
    print(m.groups())


# Discussion

m = datepat.match('11/27/2012abcdef')
m
m.group()
# '11/27/2012'

# If you want an exact match, make sure the pattern includes the end-marker ($), as in the following:

datepat = re.compiler(r'(\d+)/(\d+)/(\d+)$')
datepat.match('11/27/2012abcedef')
datepat.match('11/27/2012')

# --
re.findall(r'(\d+)/(\d+)/(\d+)', text)
