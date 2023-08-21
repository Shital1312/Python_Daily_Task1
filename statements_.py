a = 10
if a == 9:
	print(9)
elif a == 8:
	print(8)
else:
	print("Nothing")

list1 = ["Name", "age"]
list2 = ['Siya', '23']
for a, b in zip(list1, list2):
	print(a, b)
# for i in range(len(list1)):
# 	if i < len(list2):
# 		print(list1[i])
# 	print(list2[i])

list3 = ['name', 'course', 'age']
for index, value in enumerate(list3):
	print(f"{index} ---->{value}")

dict1 = {'a': 1, 'b': 2, 'c': 3}
for i in dict1:
	print(i)

# for i in dict.values(dict1):
# 	print(i)

for i in dict.keys(dict1):
	print(f"{i}----> {dict1[i]}")

for i, v in dict.items(dict1):
	print(i, v)

for i in range(2):
	for j in range(2):
		print(i, j)

# break, continue, pass
for i in range(5):
	if i == 3:
		continue
	print(i)

# break, continue, pass
for i in range(5):
	if i == 3:
		break
	print(i)

x = 5
if x == 3:
	print(x)
elif x == 4:
	pass
elif x == 5:
	print("It's correct")
else:
	print('Yes')


for i in range(3):
	print(i)
else:
	print("It's work")
#
# if __name__ == '__main__':
# 	n = int(input("enter:"))
# 	arr = map(int, input("NUber:").split(' '))
# 	arr = sorted(arr)
# 	print(arr[-2])

for i in range(1,6):
	for j in range(1, i+1):
		print('*', end='')
	print()
