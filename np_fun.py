from numpy import *
# zeros
ar_zero = zeros(5)
ar_zero1 = zeros((3,5)) # 2d
print(ar_zero)
print()
print(ar_zero1.ndim)


# ones
one = ones(5)
ones1 = ones((2,5)) # 2D
print(one)
print()
print(ones1)
print(ones1.ndim)

#Empty
na = empty(4)
print(na)

# Range
ar_range = arange(4)
print(ar_range)

# Diagonal
# ar = eye(3)
ar = eye(3,5)
print(ar)

# linspace
ln = linspace(1,10,5)
print(ln)