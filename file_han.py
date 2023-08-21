# with open("First.txt", 'w') as f:
# 	str = input('Enter Text: ')
# 	f.write(str)
# 	f.close()
#
# with open("First.txt", 'r')as f:
# 	str = f.read()
# 	print(str)
# 	f.close()

# f = open("First.txt", 'w')
# print("enter text (@ at end)")
# while str != '@':
# 	str = input()
# 	if(str != '@'):
# 		f.write(str+'\n')
#
# f.close()
# f = open("First.txt", 'r')
# line = f.read()
# print(line)
# f.close()
f = open("First.txt", 'a+')
print("Added new line.")
st = ''
while st != '@':
	# print("STOP")
	st = input()
	if st != '@':
		f.write(st+'\n')
	else:
		break


f.seek(0,0)

line = f.read()
print(line)
f.close()

