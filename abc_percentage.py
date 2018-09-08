# "the program finds what percentage of the text each character of the alphabet occupies"

abc = "abcdefghijklmnopqrstuvwxyz"

with open("/home/miklos/Python/SI6/myfile.csv","r") as myfile:
    read_file = myfile.read()
    caracters = {}
    percentage = {}
    for caracter in read_file:
        if caracter in abc:
            caracters.setdefault(caracter,1)
            caracters[caracter] += 1
    sum = sum(list(caracters.values()))
    for caracter in read_file:
        if caracter in abc:
            percentage.setdefault(caracter,((caracters[caracter] / sum)*100))

sorted_keys = sorted(percentage.keys())
sorted_dic = {}
for key in sorted_keys:
    sorted_dic[key] = percentage[key]

for key,value in sorted_dic.items():
    print("{0} : {1:.2f}%".format(key,value))