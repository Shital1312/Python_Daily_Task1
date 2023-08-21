def greet(fx):
	def mfx():
		print("good morning")
		fx()
		print("Thanks for watching.")

	return mfx


@greet
def hello():
	print("Hello World!")


hello()

# Generator
def mygen(x,y):
	while x <y:
		yield x
		x+=1
g = mygen(5,10)
for i in g:
	print(i, end=' ')
