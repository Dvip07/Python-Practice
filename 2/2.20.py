# Performing Text Operations on Byte Strings
# 2.20.1

data = b'Hello World'
data[0:5]
data.startswith(b'Hello')
data.split()
data.replace(b'Hello', b'Hello Cruel')

# 2.20.2
data = bytearray(b'Hello World')
data[0:5]
data.startswith(b'Hello')
data.split()
data.replace(b'Hello', b'Hello Cruel')

# 2.20.3
data = b'FOO:BAR,SPAM'
import re
re.split('[:,]', data)
re.split(b'[:,]',data)

# Discussion
a = 'Hello World'
a[0]
a[1]
b = b'Hello World'
b[0]
b[1]

# --
s = b'Hello World'
print(s)
print(s.decode('ascii'))

# --
'{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')


# --
with open('jalape\xf10.txt', 'w') as f:
    f.write('spicy')

# Get a directory listing
import os
os.listdir('.')
os.listdir(b'.')

