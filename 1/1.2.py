# Unpacking Elements from Iterables of Arbitrary Length
# 1.2.1
from audioop import avg
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle) 

# 1.2.2
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
name
email
phone_numbers

# 1.2.3
# sales_record is not defined
# *trailing_qtrs, current_qtr = sales_record
# trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
# return avg_comparison(trailing_avg, current_qtr)
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
trailing
current

# Discussion
from doctest import IGNORE_EXCEPTION_DETAIL
# from numpy import record
records = [
    ('foo', 1, 2),
    ('bar','hello'),
    ('foo', 3, 4),
]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag =='foo':
        do_foo(*args)
    elif tag =='bar':
        do_bar(*args)

# --
line = 'nobody:*:-2:-2:Unpriviledged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
uname
homedir
sh

# --
record = ('ACME', 50, 123.45, (12, 18, 2012))
# ign does not work for conda python 3.9.7 version
name, *IGNORE_EXCEPTION_DETAIL,(*IGNORE_EXCEPTION_DETAIL, year) = record
# name, *_,(*_, year) = record
name
year

# --
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
head
tail

# --
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

sum(items)
