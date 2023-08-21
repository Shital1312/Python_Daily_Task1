# for i in range(5, 0, -1):
# 	print('*' * (i))
#
# for i in range(6):
# 	print('*' * (i))
#
# n = 20
# for i in range(1, 11):
# 	print(' ' * n, end='')
# 	print('* ' * (i))
# 	n = n - 1
#
# a = 5
# while a > 0:
# 	print('*' * a)
# 	a = a - 1
# print()
# a = 1
# while a <= 5:
# 	print("*" * a)
# 	a = a + 1

#
# # For loop
# for i in range(1, 5):
# 	# print(i)
# 	for j in range(i):
# 		print(j)
# print()
# # i = 1, i < 5, i +=1:
# # j = 0, j < i, j+=1
#
#
# i = 1
# while i < 5:
# 	print(i)
# 	i += 2
#

Number = 1

while (Number <= 100):
	count = 0
	i = 2

	while (i <= Number // 2):
		if (Number % i == 0):
			count = count + 1
			break
		i = i + 1

	if (count == 0 and Number != 1):
		print(" %d" % Number, end='  ')
	Number = Number + 1
print()

