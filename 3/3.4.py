# Working with Binary, Octal and Hexadecimal Integers
# 3.4.1

x = 1234
bin(x)
oct(x)
hex(x)

# 3.4.2
format(x, 'b')
format(x, 'o')
format(x, 'x')

# 3.4.3
x = -1234
format(x, 'b')
format(x, 'x')

# 3.4.4
x = -1234
format(2**32 + x, 'b')

# 3.4.5
int('4d2', 16)
int('10011010010', 2)

# Discussion
import os
os.chmod('script.py', 0o755)


