def func1():
	n = 5
	print("n value is ", n)


def func2():
	n = 10
	print("n value is : ", n)
	func1()


func2()

# Global variable
n = 10


def fun1():
	print(n)


def fun2():
	n = 20
	print(n)
	fun1()


fun2()

var = 10


def glo_var():
	global var
	var = var + 10
	print("Global variable value after sum is: ", var)


glo_var()


##Variable lenght arguments:
# *agrs - type tuple
# ** kwargs - type dict - key value paire
def mylist(*lst):
	for num in lst:
		print(num)


mylist(2, 3, 4)


def printmarks(**kwargs):

	if (len(kwargs)== 5):
		for key, value in kwargs.items():
			print(key, value)

	else:
		print("Lenght is not match")


marklist = {'shital': 40, 'om': 50, 'Raj': 90, 'shiv': 45, 'Priya': 98}
printmarks(**marklist)

def master(normal, *args, **kwargs):
	print(normal)
	for i in args:
		print(i)

	for k, v in kwargs.items():
		print(k, v)

lst = ['om',30,40]
name = {'shital': 23, 'Priya': 12}
master('mylist', *lst, **name)




# keywod arguments

def grocery(item, price):
	print(item, price)


grocery(item="sugar", price=30)
