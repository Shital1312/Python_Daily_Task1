# from numpy import *
import numpy as np

# arr = array([10,20,30,40])
# print(type(arr))
#
# ar = array(['shital', 'shiva', 'Om'], dtype=str)
# print(ar)
#
# # creating arrays using linspace
# a = linspace(2,8,4,endpoint=True)
# print('a = ',a)

a = np.array([1, 2, 3])
print(a.ndim)  # 1 d

# l = []
# for i in range(5):
# 	user = int(input("Enter: "))
# 	l.append(user)
#
# print(np.array(l))

ar2 = np.array([[1, 2, 3, 4, ], [5, 6, 7, 8]])  # 2d
print(ar2.ndim)

ar3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [11, 12, 13, 14]]])  # 3d
print(ar3)
print(ar3.ndim)

ar4 = np.array([1, 2, 3, 4], ndmin=10)  # multi D
print(ar4)
print(ar4.ndim)
