# Interpolating variables in strings
# 2.15.1

s = '{name} has {n} messages.'
s.format(name='Guido', n=37)

# 2.15.2
name = 'Guido'
n = 37
s.format_map(vars())

# 2.15.3
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
s.format_map(vars(a))


# 2.15.4
s.format(name='Guido')

# --
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


# --
del n   # Make sure n is undefined
s.format_map(safesub(vars()))

# 2.15.5
import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favourite color is {color}'))


# Discussion
name = 'Guido'
n = 37
'%(name) has %(n) messages.' % vars()

# --
import string 
s = string.Template('$name has $n messages.')
s.substitute(vars())
