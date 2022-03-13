# Working with Unicode Characters in Regular Expression
# 2.10.1

import re
num = re.compile('\d+')
# ASCII digits
num.match('123')

# Arabic digits
num.match('\u0661\u0662\u0663')

# --
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

# 2.10.2
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s)

pat.match(s.upper())  # Doesn't watch
s.upper()  # Case folds