# coins = [1,1,1,1,0,1,1,1]
import random


def measuring_coins(coins, measurement_count):
    if coins == [0]:
        return measurement_count
    # if len(coins) == 3:
    #     return measurement_count + 1
    measurement_count += 1
    stack1 = coins[:(round(len(coins)/2))]
    stack2 = coins[(round(len(coins)/2)):]
    if min(stack1) == 0:
        coins = stack1
        print("stack1")
    else:
        coins = stack2
        print("stack2")
    return measuring_coins(coins, measurement_count)


def how_many_measurements(n):
    coins = []
    measurement_count = 0
    for coin in range(n):
        coins.append(1)
    coins[random.randint(0, n-1)] = 0
    print(coins)
    return measuring_coins(coins, measurement_count)


print(how_many_measurements(5))