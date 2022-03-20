# Calculating with Fractions
# 3.8.1
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a * b)

# Getting numerator/denominator
c = a * b
c.numerator
c.denumerator

# Converting to a float
float(c)

# limiting the denominator of a value
print(c.limit_denominator(8))

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
y