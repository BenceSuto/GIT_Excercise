hive = [["b", "e", "e", ".", "b", "e", "e"],
        ["e", ".", "e", ".", "e", ".", "e"],
        ["e", "e", "b", ".", "e", "e", "b"]]


def how_many_bees(hive):
    for row in range(len(hive)):
        hive[row] = "".join(hive[row])
    print(hive)


how_many_bees(hive)
