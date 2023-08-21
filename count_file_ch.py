f = open('First.txt', 'r')
# a = f.write("This is program\nThis is python 3.9\nadded @345*#")
line = f.read()
# ch = line.split(' ')
# print(len(ch))
# print(ch)
# count alphabets, numbers and space=
# a, b,c,d = 0,0,0,0
# for i in line:
# 	if i.isalpha():
# 		a += 1
# 	elif i.isdecimal():
# 		b += 1
# 	elif i.isspace():
# 		c +=1
# 	else:
# 		d+=1
#
# print(f"alphabets is = {a}\nnumbers is = {b}\nspace count is = {c}\nspecial characters is = {d}")
# count vowles and const

v,c = 0,0
for ch in line:
	if ch in ['a', 'e', 'i', 'o', 'u']:
		v+=1
	elif ch.isalpha():
		c+=1

print(f'Vowles are {v}\nconstant are {c}')

f.close()