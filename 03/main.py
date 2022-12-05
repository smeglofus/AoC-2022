

with open('\\Users\\Dell\\Desktop\\AoC2022\\03\\data.csv', 'r') as f:
    obsah = f.readlines()

all_priority = 0

for line in obsah:
    firstpart, secondpart = set(line[:len(line) // 2]), set(line[len(line) // 2:])
    prebejva = firstpart.intersection(secondpart)
    for char in prebejva:
        if char.islower():
            prior = ord(char) - 96
            all_priority += prior
        else:
            prior = ord(char) - 38
            all_priority += prior


print(all_priority)

all_priority = 0

for index,line in enumerate(obsah):
    if index % 3 == 0:
        firstpart, secondpart, thirdpart = set(obsah[index - 3].strip('\n')), set(obsah[index - 2].strip('\n')), set(obsah[index - 1].strip('\n'))
        prebejva = firstpart.intersection(secondpart,thirdpart)
        print(prebejva)
        for char in prebejva:
            if char.islower():
                prior = ord(char) - 96
                all_priority += prior
            else:
                prior = ord(char) - 38
                all_priority += prior

print(all_priority)