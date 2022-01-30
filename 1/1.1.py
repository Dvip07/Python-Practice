# Unpacking a Sequence into seperate variables
# 1.1.1

p=(4,5)
x,y = p
x
y

# 1.1.2
data = ['ACME',50,91.1,(2012, 12, 21) ]
name, share, price, date = data
name
date

# 1.1.3
name, share, price, (year, mon, day) = data
name
year
mon
day

# Discussion
s = 'Hello'
a,b,c,d,e = s
a
b
e

# --
data = ['ACME',50, 91.1, (2012,12,21) ]
_,shares, price, _ = data
shares
price
