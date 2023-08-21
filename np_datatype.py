import numpy as np


ar = np.array([1,2,3,4])
print("data type: ", ar.dtype)
print('*'*20)
ar1 = np.array([1.2, 2.4, 5.5])
print("data type: ", ar1.dtype)
print('*'*20)

ar2 = np.array([1,2,3,4], dtype=np.int8)
print("data type: ", ar2.dtype)
print('*'*20)

ar3 = np.array([1,2,3,4, 'a', 'b'])
print("data type: ", ar3.dtype)
print('*'*20)

ar4 = np.array([1,2,3,4],'f')
print("data type: ", ar4.dtype)
print('*'*20)

ar5 = np.array([1,2,3,4])
print(ar5.dtype)
print('*'*20)
# convert data type
new = np.float32(ar5)
print(new)
print('*'*20)

print(new.dtype)
print('*'*20)

nw = np.int_(new)
print(nw.dtype)
print('*'*20)
x = np.array([1,2,3,4])
x1 = x.astype(float)
print(x1)
print(x1.dtype)
a = np.array(['shital', 'om'])
print(a.dtype)

