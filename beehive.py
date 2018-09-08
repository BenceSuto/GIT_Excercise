hive = [["b", "e", "e", ".", "b", "e", "e"],
        ["e", ".", "e", ".", "e", ".", "e"],
        ["e", "e", "b", ".", "e", "e", "b"]]


def how_many_bees(hive):
    if bool(hive) is False:
        return 0
    for row in range(len(hive)):
        hive[row] = "".join(hive[row])
    bee_count = 0
    for row in hive:
        bee_count += row.count("bee")
        bee_count += row.count("eeb")
    for col in range(len(hive[0])):
        hive_col = ""
        for row in range(len(hive)):
            hive_col += hive[row][col]
        bee_count += hive_col.count("bee")
        bee_count += hive_col.count("eeb")
    return bee_count


print(how_many_bees(hive))
