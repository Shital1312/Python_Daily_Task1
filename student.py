class Student:
	def __init__(self, name, roll_no, marks):
		self.name = name
		self.roll_no= roll_no
		self.marks = marks

	def display(self):
		print(f"Name is {self.name}\nRoll no is {self.roll_no}\nmarks is {self.marks}")