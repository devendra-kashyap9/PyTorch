import torch

# ============================================
#              TENSOR RESHAPING
# ============================================

x = torch.arange(9)
x_3x3 = x.view(3, 3)     # must be contiguous in memory
x_3x3 = x.reshape(3, 3)  # safer
print(x_3x3)

y = x_3x3.t()
print(y.contiguous().view(9)) # falattening

x1 = torch.rand((2, 5))
x2 = torch.rand((2, 5))
print(torch.cat((x1, x2), dim=0).shape)  # conctenate
print(torch.cat((x1, x2), dim=1).shape)

z = x1.view(-1) # flatten
print(z.shape)

batch = 64
x = torch.rand((batch, 2, 5))
z = x.view(batch, -1) 
print(z.shape)

z = x.permute(0, 2, 1)  # transpose is speceial case of permute
                        # switchinh the dimension or switching batch, row, column position
print(z.shape)

x = torch.arange(10)
print(x.unsqueeze(0).shape)
print(x.unsqueeze(1).shape)

x = torch.arange(10).unsqueeze(0).unsqueeze(1) # 1x1x10
print(x.shape)

z = x.squeeze(1)
print(z.shape)