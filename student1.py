import student, pickle
f = open('stu_info.txt','wb')

n = int(input("Enter number of students: "))
for i in range(n):
	name = input("Enter name: ")
	roll_no = int(input('Enter roll number: '))
	marks = float(input('Enter marks: '))
	obj = student.Student(name, roll_no, marks)
	pickle.dump(obj,f)

print("Objects stored success")
f.close()