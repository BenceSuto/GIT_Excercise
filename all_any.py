nums= [55,44,33,22,11]

print([i > 5 for i in nums])

if all([i > 5 for i in nums]):
    print("yes")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")