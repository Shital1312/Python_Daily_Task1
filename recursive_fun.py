def factorial(n):
	if n == 0:
		return 1

	else:
		result = n*factorial(n-1)
		return result

for i in range(1,6):
	print("Factorial of {} is {} ".format(i, factorial(i)))

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
#
# n = int(input("Enter a number: "))
# result = factorial(n)
# print("Factorial of {} is {}".format(n, result))
print(factorial(3))


#
# def fibonacci(n):
# 	if (n == 1 or n == 0):
# 		return n
# 	else:
# 		return fibonacci(n-1)+fibonacci(n-2)
# a = int(input("NUMber: "))
# for i in range(a):
# 	print(fibonacci(i))