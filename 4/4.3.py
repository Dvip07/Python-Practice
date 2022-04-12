# Creating New Iteration Patterns with Generators
# 4.3.1

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment
for n in frange(0, 4, 0.5):
    print(n)
    
# Discussion
def countdown(n):
    print('Starting to count from ', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# Create the generator, notice no output appears
c = countdown(3)
c

# Run to first yield and emit a value
next(c)

# Run to the next yield
next(c)

# Run to the next yield
next(c)

# Run to the next yield
next(c)

