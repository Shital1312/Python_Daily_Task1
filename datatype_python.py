a = 10
b = 10
print(id(a))
print(id(b))
b = True
print(id(b))
print(int(b))

a = bin(10)
v = int('1010', 2)
print(v)
print(a)
b = hex(10)
print(b)
a = 10
print(oct(a))