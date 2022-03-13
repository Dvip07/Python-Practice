# Stripping Unwanted Characters from Strings
# 2.11.1

# Whitespace stripping
s = '   hello world  \n'
s.strip()
s.lstrip()
s.rstrip()

# Character stripping
t = '-------hello======'
t.lstrip('-')
t.strip('-=')

# Discussion
s = '   hello       world   \n'
s = s.strip()
s

# --
s.replace(' ', '')
from fileinput import filename
import re
re.sub('\s+', ' ', s)

# --
with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        return

        
