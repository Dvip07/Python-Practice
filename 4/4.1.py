# Manually Consuming an Iterator
# 4.1.1

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass
    
# 4.1.2
with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end= '')
        
# Discussion

items = [1, 2, 3]
# Get the iterator
it = iter(items)
# Run the iterator
next(it)
next(it)
next(it)
next(it) # it will throw an error


    