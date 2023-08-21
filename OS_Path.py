import os, sys

fname = input("Enter filename: ")
if os.path.isfile(fname):
	f = open(fname, 'r')

else:
	print(fname + ' does not exist')
	sys.exit()

print("The file contents are: ")
line = f.read()
print(line)
f.close()
