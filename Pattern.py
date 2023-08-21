for i in range(5):
	for j in range(5):
		print('*', end= '')
	print()

for i in range(6):
	for j in range(i):
		print('*', end='')
	print()
print()
n = 5
for i in range(n):
	for j in range(n-i):
		print('*', end='')
	print()

for i in range(1,6):
	for j in range(1, i+1):
		print('*', end='')
	print()

for i in range(5):
	for j in range(i, 5):
		print(' ', end='')
	for j in range(i+1):
		print('*', end='')
	print()

for i in range(5):
	for j in range(i+1):
		print(' ', end='')
	for j in range(i, 5):
		print('*', end='')
	print()

n = 5
for i in range(n):
	for j in range(i, n):
		print(' ', end='')
	for j in range(i+1):
		print('*', end='')
	for j in range(i+1):
		print('*', end='')
	print()

n = int(input("Enter the how many rows you want: "))
for i in range(n):
	for j in range(i+1):
		print(j+1, end=' ')
	print()