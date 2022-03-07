# Transforming and Reducing Data at the same time
# 1.19.1

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# Determine if any .py files exist in a Directory
import os
files = os.listdir('dirname')
if any(name.endswith('py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a Data Structure
portfolio = [
    {'name': 'GOOG', 'shares': 50}
    {'name': 'YHOO', 'shares': 75}
    {'name': 'AOL', 'shares': 20}
    {'name': 'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)

# Discussion
nums = 1 # Declared nums for no error
s = sum((x * x for x in nums))
s = sum(x * x for x in nums)

# --
nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])

# --
min_shares = min(s['shares'] for s in portfolio)

min_shares = min(portfolio, key=lambda s: s['shares'])

