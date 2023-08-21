lst = [10, 23, 35, 15, 7]
print(lst)
for j in range(len(lst)-1):
	for i in range(len(lst)-1-j):
		if lst[i] > lst[i+1]:
			lst[i], lst[i+1] = lst[i+1], lst[i]
			# print(lst)
print("Sorted list: ", lst)


print("Desending order:  bubble sort")
lt = []
x = int(input("Enter how many ele add in list: "))
for i in range(x):
	lt.append(int(input("Add the number: ")))

print(lt)
for j in range(len(lst)-1,-1):
	for i in range(j):
		if lt[i] > lt[i + 1]:
			lt[i], lt[i + 1] = lt[i + 1], lt[i]
	# print(lst)
	print("Sorted list: ", lt)