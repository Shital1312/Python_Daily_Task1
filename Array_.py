# import array as a
from array import *

a = array('i', [1, 2, 3])
print(len(a))

c = array('u', ['a', 'b'])
c.append('c')
print(c)
e = array('d', [2.3, 4.5, 2.0])
print(c.count('a'))
d = array('u', ['e', 'F'])
c.extend(d)
print(c)
a = ['s', 'x']
c.fromlist(a)
print(c)
y = array('i', [10, 20, 30])
y.insert(1, 40)
print(y)
y.reverse()
print(y)
y.remove(10)
print(y)
s = y.tolist()
print(s)
print('*' * 10)
lst = [int(i) for i in input("Enter the marks: ").split()]
marks = array('i', lst)
sum = 0
for x in marks:
	sum += x

print("Total marks: ", sum)
n = len(marks)
avg = sum / n
print("Average of marks: -->", avg)
