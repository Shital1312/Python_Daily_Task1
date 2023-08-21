# Assign a function to a variable
def display(str):
	return 'Hello ' + str

obj = display("Ram")
print(obj)


def avg(a,b,c):
	return a+b+c/len([a,b,c])


result = avg(20,30,40)
print(result)
# define a function inside another function
def display1(str):
	def meg():
		return 'How are you? '
	result = meg()+str
	return result

print(display1("OM"))