# Working with Infinity and NaNs
# 3.7.1
a = float('inf')
b = float('-inf')
c = float('nan')
a
b
c

# 3.7.2
import math
math.isinf(a)
math.isnan(c)

# 3.7.3
a = float('inf')
a + 45
a * 10
10 / a

# 3.7.4
a = float('inf')
a/a
b = float('-inf')
a + b

# 3.7.5
c = float('nan')
c + 23
c / 2
c * 2
math.sqrt(c)

# 3.7.6
c = float('nan')
d = float('nan')
c == d
c is d