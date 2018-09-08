def how_much_i_love_you(nb_petals):
    # dic = {1:"i love you", 2:"a litte", 3:"a lot", 4: "passionatley", 5:"madly", 6:"not at all"}
    sentences = ["i love you", "a litte", "a lot", "passionatley", "madly", "not at all"]
    nb_petals = nb_petals % 6
    if nb_petals == 0:
        return sentences[5]
    for num in range(nb_petals):
        return sentences[nb_petals-1]


print(how_much_i_love_you(12))
