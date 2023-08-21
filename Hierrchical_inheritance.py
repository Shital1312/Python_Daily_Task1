# only one parent class and multiple child classes but each child class can access parent class property.

class School:
	school = "KES high school"

	def sch(self):
		print("My school name is ", self.school)


class Jr(School):
	def div(self):
		print("I am junior ", self.school)


class Sr(School):
	def div(self):
		print("I am senior ", self.school)

j = Jr()
s = Sr()
j.div()
j.sch()
s.div()
s.sch()