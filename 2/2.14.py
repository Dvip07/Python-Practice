# Combining and Concatenating Strings
# 2.14.1
from calendar import c


parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)
','.join(parts)
''.join(parts)

# 2.14.2
a = 'Is Chicago'
b = 'Not Chicago?'
a + ' ' + b

# --
print('{} {}'.format(a,b))
print(a + ' ' + b)

# --
a = 'Hello' 'World'
a

# Discussion
s = ''
for p in parts:
    s += p

# --
data = ['ACME', 50, 91.1]
','.join(str(d) for d in data)

print(a + ':' + b + ':' + c)   #Ugly
print(':'.join([a, b, c]))  # Still Ugly
print(a, b, c, sep=':')

# --
chunk1 = 1 #Just for the Avoiding error
chunk2 = 2 #Just for the Avoiding error
# Version 1 (string concatentation)
f.write(chunk1 + chunk2)

# Version 2 (separate I/O operations)
f.write(chunk1)
f.write(chunk2)


# --
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


text = ''.join(sample())

for part in sample():
    f.write(part)

# --
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)

for parts in combine(sample(), 32768):
    f.write(part)

