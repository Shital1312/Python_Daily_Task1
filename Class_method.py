class Student:
	def __init__(self):
		self.name = 'shiva'
		self.age = 32
		self.salary = 10000

	def talk(self):
		print("i am ", self.name)
		print("I am ", self.age)
		print("My salary is ", self.salary)


s1 = Student()
s1.talk()


class Emp:
	def __init__(self, name, second, pay):
		self.fname = name
		self.lname = second
		self.pay = pay
		self.email = name + '.' + second + "@company.com"

	def fullname(self):
		return f"Full name is {self.fname} {self.lname}"


emp1 = Emp('shital', 'Pawar', 20000)
emp2 = Emp('Prem', 'Patil', 30000)
print(emp1.email)
print(emp2.pay)

print(emp1.fullname())


class Stu:
	# this is constructor......
	def __init__(self, n='', m=()):
		self.name = n
		self.marks = m

	# this is an instance method
	def dis(self):
		print("MY name is ", self.name)
		print("MY marks is ", self.marks)


s1 = Stu("Om", 99)
s1.dis()
