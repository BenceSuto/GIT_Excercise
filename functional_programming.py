def apply_thrice(func, arg):
   return func(func(func(arg)))

def add_five(x):
   return x + 5

print(apply_thrice(add_five, 10))