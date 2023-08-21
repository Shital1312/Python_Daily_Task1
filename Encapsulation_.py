# by using encapsulations we cn restrict the variables and methods access globally by making it private and protected.
# double underscore - private
# single underscore - protected
class A:
	_a = 10 # protected
	__b = 20 # private


	def show(self):
		print(f"a = {self._a}")
		print("b = ", self.__b)


obj = A()
obj.show()
print("A Value is :", obj._a)
# print("A Value is :", obj.__b)# - b ko use nahi kar skte class ke bahar
