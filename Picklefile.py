import pickle

# pickleing data in file
f = open("abc.txt", 'wb')  # wb for write mode in binary

n = int(input("How many employees?"))
for i in range(n):
	id = int(input("Enter id number: "))
	name = input("Enter name: ")

	e = (id, name)
	pickle.dump(e, f)

f.close()

# unpickling

f = open('abc.txt', 'rb')
print("Employees details: ")
while True:
	try:
		# read object from file f
		obj = pickle.load(f)
		# obj.display()
		print(obj)

	except:
		print('End of the file reached.....')
		break

f.close()
