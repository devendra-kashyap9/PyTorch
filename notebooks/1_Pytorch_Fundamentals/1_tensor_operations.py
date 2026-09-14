import torch

print(torch.__version__)
# ============================================
#           INITIALIZING TENSORS
# ============================================

# setting up the device
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

my_tensor = torch.tensor([[1,2,3], [4,5,6]],
                         dtype=torch.float32,
                         device=device,       # can be named the device deirectly, "cuda", "mps", "cpu"
                         requires_grad=True)

print(my_tensor)
print(my_tensor.dtype)
print(my_tensor.device)
print(my_tensor.shape)
print(my_tensor.requires_grad)

# Other comkon initializing mwthod
# tensor with vales "0"
x = torch.empty(size=(3,3))
x = torch.zeros((3,3))
x = torch.rand((3,3))
x = torch.ones((3,3))
x = torch.eye(3,3)  # Identity Matrix
x = torch.arange(start=0, end=5, step=1)
x = torch.arange(0,5,2)
x = torch.linspace(start=0.1, end=1, steps=10)
x = torch.empty(size=(3,3)).uniform_(0, 1)
x = torch.empty(size=(3,3)).normal_(mean=0, std=1)
x = torch.diag(torch.ones(3)) # diagonal matrix
print(x)

# How to Initialize and convert tensors to other types (int, float, double)
tensor = torch.arange(4)
print(tensor.dtype)
print(tensor.bool().dtype)
print(tensor.short().dtype)  # int16
print(tensor.long().dtype)  # int64 (Important)
print(tensor.half().dtype)  # float16
print(tensor.float().dtype)  # float32 (Important)
print(tensor.double().dtype)  # float64

# Array to tensor conversion and vice-versa
import numpy as np
np_array = np.zeros((5,5))
tensor = torch.from_numpy(np_array)
np_back = tensor.numpy()
print(type(np_array))
print(type(tensor))
print(type(np_back))