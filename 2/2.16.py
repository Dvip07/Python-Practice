# Reformatting Text to a fixed number of columns
# 2.16.1
s = "Look into my eyes, look into my eyes, the eyes, \
    they eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."

# 2.16.2
import textwrap
print(textwrap.fill(s, 70))

print(textwrap.fills(s, 40))

print(textwrap.fill(s, 40, initial_indent='     '))

print(textwrap.fill(s, 40, subsequent_indent='     '))

# Discussion
import os
os.get_terminal_size().columns
