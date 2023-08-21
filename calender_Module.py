# from calendar import *
# #check year is leap or not
# y = int(input("Enter year: "))
# if isleap(y):
# 	print(y, 'Is leap year')
# else:
# 	print(y, 'Is not leap')
#
# #to display calender of given month of the year
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))
# cal = month(yy, mm)
# print(cal)


#second max number in list
# if __name__ == '__main__':
#     n = int(input())
#     arr = set(map(int, input().split()))
#     arr1 = list(sorted(arr))
#     max_num = arr1[-2]
#     print(max_num)

# if __name__ == '__main__':
# 	student = []
# 	for _ in range(int(input())):
#
# 		name = input("Enter a name: ")
# 		score = float(input("Enter score: "))
# 		stu = [name, score]
# 		student.append(stu)
#
# 	for s in student:
# 		print(s[0], s[1])
if __name__ == '__main__':
	x = int(input())
	y = int(input())
	z = int(input())
	n = int(input())

	l = list(
		[i, j, k]

		for i in range(0, x + 1)
		for j in range(0, y + 1)
		for k in range(0, z + 1)

		if not (i + j + k) == n
	)

	print(l)
