# Mapping Keys to Multiple Values in a Dictionary
# 1.6.1

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}

# 1.6.2
from collections import defaultdict
from itertools import pairwise
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d.defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(4)

# 1.6.3
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)


# Discussion
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# --
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

