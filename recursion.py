

def bigger_fish(func, health):
    return func(func, health)


def recur(func, health):
    health -= 1
    print("arghh")
    if health != 0:
        return func(func, health)
    else:
        return health


print(bigger_fish(recur, 5))
