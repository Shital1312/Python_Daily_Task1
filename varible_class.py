# instance variable example

class Sample:
	# this is constructor
	def __init__(self):
		self.x = 10

	# this is instance method
	def modify(self):
		self.x += 1


# create 2 instances


s1 = Sample()
s2 = Sample()
print("x in s1 = ", s1.x)
print("x in s2 = ", s2.x)

# modify x in s1
s1.modify()
print("x in s1 = ", s1.x)
print("x in s2 = ", s2.x)
print()


# instance class variable example

class Sample:
	x = 10  # this is a class variable

	# this is constructor

	# this is class method
	@classmethod  # this is a decorator
	def modify(cls):  # cls must be the first parameter
		cls.x += 1  # cls.x refers to class variable x


# create 2 instances


s1 = Sample()
s2 = Sample()
print("x in s1 = ", s1.x)
print("x in s2 = ", s2.x)

# modify x in s1
s1.modify()
print("x in s1 = ", s1.x)
print("x in s2 = ", s2.x)
