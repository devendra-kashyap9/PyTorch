import torch

# ============================================
#                 TENSOR MATH
# ============================================

x = torch.tensor([1,2,3])
y = torch.tensor([9,8,7])

# Addition
z1 = torch.empty(3)
torch.add(x, y, out=z1)
print(z1)

z2 = torch.add(x ,y)
z = x + y

# Subtraction
z = x - y

# Division
z = torch.true_divide(x, y)  # vectorised operation of x and y
z = torch.true_divide(x, 2)  # if scalar then divide each elements of x by a scalar

# inplace operation
t = torch.zeros(3)
t.add_(3)  # any operation followed by "_" is inplace op
t += 3  # t = t + 3 i s not inplace, we'll create copy first

# Exponentiation
z = x.pow(2)
z = x ** 2

# Simple Comparison
z = x > 2

# Matrix Multiplication
x1 = torch.rand((2, 5))
x2 = torch.rand((5, 3))
x3 = torch.mm(x1, x2)
x3 = x1.mm(x2)

# matrix exponentiation
matrix_exp = torch.rand((5,5))
print(matrix_exp.matrix_power(3))  # cube of matrix or matrix ^ 3

# element wise multiplication
z = x * y
print(z)

# dot product
z = torch.dot(x, y)
print(z)

# Matrix batch multiplication
batch = 32
n = 10
m = 20
p = 30

tensor_1 = torch.rand((batch, n , m))
tensor_2 = torch.rand((batch, m, p))
out_bmm = torch.bmm(tensor_1, tensor_2) # (batch, n, p)
print(out_bmm)

# Example of BroadCasting
x1 = torch.rand((5, 5,))
x2 = torch.rand((1, 5))

z = x1 - x2
z = x1 - 5
z = x2 - 3
z = x1 ** x2
print(z)

# Other useful tensor operations
sum_x = torch.sum(x1, dim=0)
values, indices = torch.max(x1, dim=1)
values, indices = torch.min(x1, dim=1) # could be print(max(x), min(x))
abs_x = torch.abs(x)
z = torch.argmax(x, dim=0)
z = torch.argmin(x, dim=0)
mean_x = torch.mean(x.float(), dim=0)  # for calculating meand PyTorch requires float value
z = torch.eq(x ,y)  # checks elementWise Equality
sorted_y, indices = torch.sort(y, dim=0, descending=False)

'''torch.clamp is a PyTorch function used to restrict all elements of a tensor within a specified 
minimum and maximum range.
        torch.clamp(input, min=None, max=None, *, out=None)'''

z = torch.clamp(x, min=0, max=5)
z = torch.clamp(y, min=0, max=5) # y = [9,8,7]
z = torch.clamp(torch.tensor([-5,4,7,8]), min=0, max=5)

x = torch.tensor([1,2,4,0,3,0,-5], dtype=torch.bool)
z = torch.any(x)  # True
z = torch.all(x)  # False




