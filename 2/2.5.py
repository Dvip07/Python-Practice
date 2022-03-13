# Searching and Replacing Text
# 2.5.1

text = 'yeah, but no, but yeah, but no, but yeah'

text.replace('yeah', 'yep')

# 2.5.2
text = 'Today is 11/27/2012. Pycon starts 3/13/2013.'
import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

# 2.5.3
import re
datepat = re.compiler(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'3-\-1\-2', text)
# Today is 2012-11-27. Pycon starts 2013-3-13

# 2.5.4
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{}-{}-{}'.format(m.group(2), mon_name, m.group(3))

datepat.sub(change_date, text)

# 2.5.5
newtext, n = datepat.subn(r'\3-\1-\2', text)
newtext
n