
import re

with open('\\Users\\Dell\\Desktop\\AoC2022\\04\\data.csv', 'r') as f:
    obsah = f.read().splitlines()


seznam = []
for line in obsah:
    toto = re.split('-|,',line)
    seznam.append(toto)


fits = 0
for line in seznam:
    if int(line[0]) in range(int(line[2]), int(line[3]) + 1) or int(line[1]) in range(int(line[2]), int(line[3]) + 1):
        fits += 1
    elif int(line[2]) in range(int(line[0]), int(line[1]) + 1) or int(line[3]) in range(int(line[0]), int(line[1]) + 1):
        fits += 1
print(fits)