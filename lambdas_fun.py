f = lambda x: x * x
val = f(5)
print(val)

add = (lambda x, y: x + y)(2, 3)
print(add)
# result = add(2,3)
# print(result)

lst = [2, 3, 4, 5, 6]
lst1 = list(filter(lambda x: x % 2 == 0, lst))
print(lst1)

lt = filter(lambda x: x % 2 == 0,[2,3,4,5])
print(list(lt))

# lambda with map()
def squ(x):
	return x*x

lst = [2,3,4,5]
lst1 = map(squ, lst)
print(list(lst1))

lst = [2,4,6]
ls1 = map(lambda x : x*x, lst)
print(list(ls1))

lt1 = [2,3,4,5]
lt2 = [6,7,8,9]
lt3 = list(map(lambda x, y: x*y, lt1, lt2))
print(lt3)