# Matching Text at the Start or End of a String
# 2.2.1

filename = 'spam.txt'
filename.endswith('.txt')
filename.startwith('file')
url = 'http://www.python.org'
url.startwith('http:')

# 2.2.2
import os
filenames = os.listdir('.')
filenames
[name for name in filenames if name.endswith(('.c', '.h'))]
any(name.endswith('.py') for name in filenames)

# 2.2.3
from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# 2.2.4
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
url.startswith(choices)

# Discussion
filename = 'spam.txt'
filename[-4:] == '.txt'
url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'

# --
import re
url = 'http://www.python.org'
re.match('http:|https:|ftp:', url)

# --
if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
    ...
    

