#xyz= 123


with open('\\Users\\Dell\\Desktop\\AoC2022\\02\\data.csv', 'r') as f:
    obsah = f.readlines()

"""
A = kamen    X = Prohra
B = papir    Y = remiza
C = Nuzky    Z = Výhra
"""

rock = ("A Y\n","B X\n","C Z\n")
papper = ("A Z\n","B Y\n","C X\n")
scissors = ("A X\n","B Z\n","C Y\n")

score = 0
for line in obsah:
    if line in rock:
        score += 1
    if line in papper:
        score += 2
    if line in scissors:
        score += 3
    if "X" in line:
        score += 0
    if "Y" in line:
        score += 3
    if "Z" in line:
        score += 6
print(score)



