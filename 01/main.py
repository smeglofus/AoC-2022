
import csv
with open('\\Users\\Dell\\Desktop\\AoC2022\\01\\data.csv', 'r') as f:
    obsah = f.readlines()

max = []
cislo = 0

for number in obsah:
    if len(number) > 2:
        cislo += int(number)
    if len(number) < 2:
        max.append(cislo)
        cislo = 0

max_num = sorted(max)[-1]
max_three = sum(sorted(max)[-3:])

print(max_num)
print(max_three)