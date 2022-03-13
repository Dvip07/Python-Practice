# Splitting Strings on Any of Multiple Delimiters
# 2.1.1

line = 'asdf fjdk; afed, fjek,asdf,       foo'
import re
re.split(r'[;,\s]\s*', line)
# ['asdf', 'fjdk', 'afdk', 'fjek', 'asdf', 'foo']

# Discussion
fields = re.split(r'(;|,|\s)\s*', line)
fields

# --
values = fields[::2]
delimiters = fields[1::2] + ['']
values
delimiters

# --
# Reform the line using the same delimiters
''.join(v+d for v,d in zip(values, delimiters))

# --
re.split(r'(?:,|;|\s)\s*', line)
