# Removing Duplicates from a Sequence while Maintaing Order
# 1.10.1
from re import A
from typing import DefaultDict


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# 1.10.2
a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a))

# 1.10.3
def dedupe(items, key=None):
    seen = set()
    for items in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# 1.10.4
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dedupe(a, key=lambda d: (d['x'],d['y'])))
list(dedupe(a, key=lambda d: d['x']))

# Discussion
a
set(a)

# --
with open(somefile, 'r') as f:
    for line in dedupe(f):