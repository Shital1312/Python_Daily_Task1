max = int(input("Enter the max number: "))
for num in range(2, max + 1):
	for i in range(2, num):
		if num % i == 0:
			break
	else:
		print(num)

for i in range(2, 10):
	if i % 2 == 0:
		print(i ** 3)
	else:
		pass
num = [int(x ** 2) if int(x) % 2 == 0 else int(x) ** 3 for x in range(10)]
print(num)
odd_num = [int(x) for x in range(10) if int(x) % 2 != 0]
print(odd_num)


# # prime number
# def prime(n):
# 	x = 1
# 	for i in range(2, n):
# 		if n % 2 == 0:
# 			x = 0
# 			break
# 		else:
# 			x = 1
# 	return x
#
#
# num = int(input("number: "))
# result = prime(num)
# if result == 1:
# 	print(num, 'Is prime')
# else:
# 	print(num, 'It is not Prime')

#
# def prm(n):
# 	x = 1
# 	for i in range(2, n):
# 		if n % i == 0:
# 			x = 0
# 			break
# 		else:
# 			x = 1
# 	return x
#
#
# i = 2
# c = 1
# num = int(input("how many prime numbers you want to see:"))
# while True:
# 	if prm(i):
# 		print(i)
# 		c += 1
# 	i += 1
# 	if c > num:
# 		break


def Is_prime(num):
	# num = int(input("Enter a num: "))

	if num < 2:
		print('its not prime')
	else:
		for i in range(2, num):
			if num % i == 0:
				# print(num, "It's not prime")
				return False
			# break
		else:
			return True
		# print(num, "It's prime")


# Is_prime()
count = 0
for i in range(2, 100):
	if Is_prime(i):
		count += 1
print(count)
# 	print(i, "Prime")
# else:
# 	print(i, "Not prime")


print()
num = int(input("Enter a number: "))
i = 2
if num == 2:
	print("It's prime")
elif num <= 1:
	print("Not prime")
else:
	while i * i <= num:
		if num % i == 0:
			print(num, "Not prime")
			break
		i += 1

	else:
		print(num, "Prime")
