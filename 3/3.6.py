# Performing Complex-Valued Math
# 3.6.1
a = complex(2, 4)
b = 3 -5j
a
b

a.real
a.imag
a.conjugate

# 3.6.2
a + b
a * b
a / b
abs(a)

# 3.6.3
import cmath
cmath.sin(a)
cmath.cos(a)
cmath.exp(a)

# Discussion
import numpy as np
a = np.array([2+3.j, 4+5.j, 6-7.j, 8+9.j])
a
a + 2
np.sin(a)

# --
cmath.sqrt(-1)

