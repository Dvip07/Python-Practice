# Aligning Text Strings
# 2.13.1

text = 'Hello World'
text.ljust(20)
text.rjust(20)
text.center(20)

# 2.13.2
text.rjust(20, '=')
text.center(20, '*')

# 2.13.3
format(text, '>20')
format(text, '<20')
format(text, '^20')

# 2.13.4
format(text, '=>20s')
format(text, '*^20s')

# 2.13.5
'{:>10s} {:>10s}'.format('Hello', 'World')

# --
x = 1.2345
format(x, '>10')
format(x, '^10.2f')

# Discussion
'%-20s' % text
'%20s' % text

