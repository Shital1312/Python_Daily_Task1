import numpy as np
var = np.array([[1,2,3],[5,6,7]])
print(var)
print(var.shape)
print()
v = np.array([1,2,3],ndmin=5)
print(v)
print(v.ndim)
print(v.shape)
print()
# reshape
r = np.array([1,2,3,4,5,6])
x = r.reshape(3,2) # 3 means rows , 2 means coloum for 2 diretion
print(x)

a = np.array([1,2,3,4,5,6,7,8,9,11,12,13])
x1 = a.reshape(2,3,2) # 2 means rows , 3 means coloum for 2 diretion
print(x1)
print(x1.ndim)
print()
re = x1.reshape(-1)
print(re)
print(re.ndim)