# Matching Strings Using Shell Wildcard Patterns
# 2.3.1

from fnmatch import fnmatch, fnmatchcase
fnmatch('foo.txt', '*.txt')
fnmatch('foo.txt', '?oo.txt')
fnmatch('Dat45.csv', 'Dat[0-9]*')
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]

# 2.3.2

# On OS X (Mac)
fnmatch('foo.txt', '*.TXT')
# False

# On Windows
fnmatch('foo.txt', '*.TXT')
# True

# --
fnmatchcase('foo.txt', '*.TXT')


# 2.3.3
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

# 2.3.4
from fnmatch import fnmatchcase
[addr for addr in addresses if fnmatchcase(addr, '* ST')]
[addr for addr in addresses if fnmatch(addr, '54[0-9][0-9] *CLARK*')]