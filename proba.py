def bigger_fish(func, arg):
	return func(func(arg))

def add_five(x):
	return x + 5

print(bigger_fish(add_five, 10))