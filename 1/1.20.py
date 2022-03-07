# Combining Multiple Mappings into a Single Mapping
# 1.20.1

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap

from cv2 import merge
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

# Discussion

len(c)
list(c.keys())
list(c.values())

# --
c['z'] = 10
c['w'] = 40
del c['x']
a
del c['y']

# --
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
values
values['x']
# Discard last mapping
values = values.parents
values['x']

# Discard last mapping
values = values.parents
values['x']
values
# ChainMap({'x': 1})

# --
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
merged['x']
merged['y']
merged['z']

# --
a['x'] = 13
merged['x']

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
merged['x']
a['x'] = 42
merged['x']
