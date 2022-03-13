# Normalizing Unicode text to a standard representation
# 2.9.1

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
s1
s2
s1 == s2
len(s1)
len(s2)

# 2.9.2
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
t1 = t2
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
t3 = t4
print(ascii(t3))

# 2.9.3
s = '\ufb01'
s
unicodedata.normalize('NFD', s)

# Notice how the combined letters are broken apart here
unicodedata.normalize('NFKD', s)
unicodedata.normalize('NFKC', s)

# Discussion
t1 = unicodedata.normalize('NFD', s1)
''.join(c for c in t1 if not unicodedata.combining(c))

