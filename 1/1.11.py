# Naming a Slice
# 1.11.1
from concurrent.futures.process import _system_limits_checked


record = '....................100          .......513.25     ..........'
cost = int(record[20.32]) * float(record[40.48])

# 1.11.2
SHARES = slice(20,32)
PRICE = slice(40,48)

cost = int(record[shares]) * float(record[PRICE])

# Discussion
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
items[2:4]
items[a]
items[a] = [10,11]
items
del items[a]
items

# --
a = slice(10, 50, 2)
a.start
a.stop
a.step

# --
s = 'HelloWorld'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])

    