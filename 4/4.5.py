# Iterating in Reverse
# 4.5.1

a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)
# Outputs 4, 3, 2, 1

# Print a file backwards
f = open('somefile')
for line in reversed(list(f)):
    print(line, end= '')
    
# Discussion
class Countdown:
    def __init__(self, start):
        self.start = start
        
    # Forward Iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
            
    # Reverse Iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n 
            n += 1
            
        