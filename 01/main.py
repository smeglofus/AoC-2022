
import csv
f = open('\\Users\\Dell\\Desktop\\AoC2022\\01\\data.csv', 'r')
obsah = f.readlines()

max = 0
cislo = 0

for number in obsah:
    if len(number) > 2:
        cislo += int(number)
    if len(number) < 2:
        if cislo > max:
            max = cislo
        cislo = 0

print(max)