import torch

# ============================================
#               TENSOR INDEXING
# ============================================

batch_size = 10
featres = 25
x = torch.rand((batch_size, featres))

print(x[0].shape) # x[0, :]
print(x[:, 0].shape)
print(x[2, 0:10])

# Fancy Indexing
x = torch.rand(10)
indices = [2, 5, 7]
print(x[indices])

x = torch.rand((3, 5))
rows = torch.tensor([1, 0])
columns = torch.tensor([4, 0])
print(x[rows, columns])

# More advanced indexing
x = torch.arange(10)
print(x[(x < 2) | (x > 8)])
print(x[x.remainder(2) == 0])

# Useful Operations
print(x)
print(torch.where(x > 5, x, x*2))  # (condition, satisfied, else)
                                   # tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
                                   # tensor([ 0,  2,  4,  6,  8, 10,  6,  7,  8,  9])
print(torch.tensor([0,0,1,1,2,3,2,4,3,2]).unique())
print(x.ndimension()) # number of dimensions
print(x.numel()) # number of elements