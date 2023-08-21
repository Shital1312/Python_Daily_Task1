import pickle

f1 = open("stu_info.txt", 'rb')
while True:
	try:
		obj = pickle.load(f1)
		obj.display()

	except EOFError:
		print("End of the file reached....")
		break

f1.close()