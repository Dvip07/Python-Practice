# Calculating with Large Numerical Arrays
# 3.9.1
# Python lists
x = [1, 2, 3, 4]  # It's just for the information 
y = [5, 6, 7, 8]  # This code contains error
x * 2
x + 10

# Numpy Errors
from matplotlib.pyplot import grid
import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
ax * 2
ax + 10
ax + ay
ax * ay

# 3.9.2
def f(x):
    return 3*x**2 - 2*x + 7
f(ax)

# 3.9.3
np.sqrt(ax)
np.cos(ax)

# 3.9.4
grid = np.zeros(shape=(10000,10000), dtype=float)
grid

# 3.9.5
grid += 10
grid
np.sin(grid)

# 3.9.6
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a

# Select row 1
a[1]

# Select column 1
a[:,1]

# Select a subregion and change it
a[1:3, 1:3]
a[1:3, 1:3] += 10
a

# Broadcast a row vector across an operation on all rows
a + [100, 101, 102, 103]
a

# Conditional assignment on an array
np.where(a < 10, a, 10)
