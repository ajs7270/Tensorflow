import numpy as np

# 1D with Numpy
t = np.array([0.,1.,2., 3.,4.,5.,6.])
print(t)

# Print State
print('Rank of t: ', t.ndim)
print('Shape of t: ', t.shape)

# Acess Data
print('t[0] t[1] = ',t[0], t[1])
print('t[2:5] = ',t[2:5])
print('t[:4] = ', t[:4])

# 2D with Numpy
t = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.],[10.,11.,12.]])
print(t)

# Print State
print('Rank of t: ', t.ndim)
print('Shape of t: ', t.shape)
