class Stu:
	# this is class var

	n = 10


# access class var in the s1 instance namespace
s1 = Stu()
print(s1.n)
s1.n += 1
print(s1.n)

s2 = Stu()
print(s2.n)
