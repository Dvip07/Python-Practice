# Performing Matrix and Linear Algebra Calculations
# 3.10.1
import numpy as np
m = np.matrix([[1, -2, 3],[0, 4, 5],[7, 8, -9]])
m

# Return transpose
m.T
# Return inverse
m.I
# Create a Vector and multiply
v = np.matrix([[2],[3],[4]])
v
m * v

# 3.10.2
import numpy.linalg
# Determinant
numpy.linalg.det(m)
# Eigenvalues
numpy.linalg.eignv(m)
# Solve for x in mx = v
x = numpy.linalg.solve(m, v)
x 
m * x
v
