# Keeping Dictionaries in Order
# 1.7.1

from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

# 1.7.2
import json
json.dumps(d)
'{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'

