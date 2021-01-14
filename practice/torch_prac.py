import torch

# 1D with Pytorch
t = torch.FloatTensor([0.,1.,2.,3.,4.,5.,6.])
print(t)

# Print State
print(t.dim())
print(t.shape)
print(t.size())

# Acess Data
print('t[0] t[1] = ',t[0], t[1])
print('t[2:5] = ',t[2:5])
print('t[:4] = ', t[:4])

# 2D with Pytorch
t = torch.FloatTensor([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.],[10.,11.,12.]])
print(t)

# Print State
print(t.dim())
print(t.size()) # == print(t.shape)


