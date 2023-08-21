import numpy as np
import random
#Rand() generate a random value between 0 to 1
var = np.random.rand(6)
print(var) # single dimention

var1 = np.random.rand(2,5)
print(var1)

# randn() generate a random value close to zero
ar = np.random.randn(4)
print(ar)

# ranf() [0.0, 1.0] less than 1 didn't inclued 1
an = np.random.ranf(2)
print(an)

#randint() generate a random number between a give range
arr = np.random.randint(2,20, 4) # min, max, total_value
print(arr)
