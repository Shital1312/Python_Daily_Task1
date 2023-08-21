import pickle

data = ['shital', 301, 25000]

# pickling

byte = pickle.dumps(data)
print(byte)

# unpickling

data1 = pickle.loads(byte)
print(data1)
