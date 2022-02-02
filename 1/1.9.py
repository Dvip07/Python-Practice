# Finding Commonalities in Two Dictionaries
# 1.9.1
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# 1.9.2
a.keys() & b.keys()

a.keys() - b.keys()

a.items() & b.items()

# 1.9.3
c = {key:a[key] for key in a.keys() - {'z', 'w'}}