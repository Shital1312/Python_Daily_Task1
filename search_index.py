# lt = []
# x = int(input("Enter how many ele add in list: "))
# for i in range(x):
# 	lt.append(int(input("Add the number: ")))
# print(lt)
# s = int(input("Enter which ele you want search: "))
#
# for i in range(x):
# 	if s == lt[i]:
# 		print("ele is found", i+1)
# 	else:
# 		pass
# if s not in lt:
# 	print("ele is not found")

from array import *

arr = array('i', [])
x = int(input("Enter how many ele add in list: "))
for i in range(x):
	arr.append(int(input("Add the number: ")))
print(arr)
s = int(input("Enter which ele you want search: "))
try:
	pos = arr.index(s)
	print("Ele is found")
except ValueError:
	print("Ele is not found.")