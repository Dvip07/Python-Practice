# Mapping Names to Sequence Elements
# 1.18.1

from collections import namedtuple
from re import S
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
sub 
sub.addr
sub.joined

# 1.18.2
len(sub)
addr, joined = sub
addr
joined

# 1.18.3
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


# --
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

# Discussion

s = Stock('ACME', 100, 123.45)
s
s.shares = 75

# --
s = s._replace(shares=75)
S

# --
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

# --
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
dict_to_stock(a)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
dict_to_stock(b)
