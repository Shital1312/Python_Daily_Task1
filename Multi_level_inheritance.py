# one parent and multiple child class

class Father:
	surname = "Patil"


class son(Father):
	def Akash(self):
		print("My mname is Akash", self.surname)


class Son2(son):
	def Ankit(self):
		print("My name is Ankit", self.surname)


s = Son2()
s.Ankit()
s.Akash()
print()


# Multiple inheritance - more parents classes and only one child class is called multiple inheritance.

class A:
	Back = 'Java and c++'

	def Backend(self):
		print("Backend Task completed using:", self.Back)


class B:
	front = "Python and HTML"

	def froned(self):
		print("Fronted Task implemented using:", self.front)


class C(A, B):
	def show(self):
		print("Task is completed")


t = C()
t.Backend()
t.froned()
t.show()
