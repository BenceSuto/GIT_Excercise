with open("/home/miklos/Python/SI6/persons_test.csv","r") as f:
#     text = f.read()
# for caracter in text:
#     print(caracter)
    text = f.readlines()
biglist = []
for rows in text:
    biglist.append(rows.strip().split(";"))

print(biglist)