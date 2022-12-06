import re
pole = []
sloupcu = 9


with open('\\Users\\Dell\\Desktop\\AoC2022\\05\\orders.csv', 'r') as f:
    ordery = f.read().splitlines()
    list_move = []
    list_from = []
    list_to = []
    for order in ordery:
        o = order.split(" ")
        list_move.append(o[1])
        list_from.append(o[3])
        list_to.append(o[5])

with open('\\Users\\Dell\\Desktop\\AoC2022\\05\\data.csv', 'r') as f:
    obsah = f.readlines()

sloupce = []


for s in range(9):
        rad = []
        for index,row in enumerate(obsah):
            toto = re.split('    | |\n',row)
            if toto[s] != '':
                rad.append(toto[s])
        sloupce.append(rad)

"""basic"""
for move in range(len(list_move)):
    for i in range(int(list_move[move])):
        ven = sloupce[int(list_from[move])-1].pop(0)
        add = sloupce[int(list_to[move])-1].insert(i, ven)

    print(sloupce)

"""harder"""
for move in range(len(list_move)):
    for i in range(int(list_move[move])):
        ven = sloupce[int(list_from[move])-1].pop(0)
        add = sloupce[int(list_to[move])-1].insert(i, ven)

    print(sloupce)



slova = []
for i in sloupce:
    slova.append(i[0].strip("[]"))

print("".join(slova))

