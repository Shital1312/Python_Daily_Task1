# single inheritance

class Bank:
	amt = 20000

	def ava(self):
		print("ava cash is ", self.amt)


class StBank(Bank):
	cash = 10000

	def ava(self):
		super().ava()
		print(self.cash + self.amt)


a = StBank()
a.ava()

#
class A:
	num1 = int(input("Enter the number: "))
	num2 = int(input("Enter the number: "))
	def add(self):
		print("additional ", self.num1+self.num2)

	def sub(self):
		print("subtraction ", self.num1- self.num2)

class B(A):
	def mul(self):
		print("MUltiplation ", self.num1*self.num2)

	def div(self):
		print("DIVISION ", self.num1/ self.num2)

obj = B()
obj.mul()
obj.div()
obj.sub()
obj.add()

obj1 = A()
obj1.add()
obj1.sub()