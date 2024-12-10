import re

file = open('input.txt', 'r')
raw_content = file.readlines()
content = []
# sorvégjelek törlése
for item in raw_content:
    content.append(item.replace("\n", ""))

xmas_count = 0
"""
# vízszintes ellenőrzés (meg kell keresni az ÖSSZES előfordulást a soron belül ---> regex!)
for item in content:
    xmas_matches = re.findall("XMAS", item)
    samx_matches = re.findall("SAMX", item)
    xmas_count += len(xmas_matches)
    xmas_count += len(samx_matches)

# függőleges ellenőrzés

#sorok
for i in range(len(content) - 3):
    # betűk soronként
    for j in range(len(content[i])):
        if content[i][j] == 'X' and content[i+1][j] == 'M' and content[i+2][j] == 'A' and content[i+3][j] == 'S':
            xmas_count += 1
        if content[i][j] == 'S' and content[i+1][j] == 'A' and content[i+2][j] == 'M' and content[i+3][j] == 'X':
            xmas_count += 1


#átlós ellenőrzés / jobbra le
for i in range(len(content) - 3):
    for j in range(len(content[i]) - 3):
        if content[i][j] == 'X' and content[i+1][j+1] == 'M' and content[i+2][j+2] == 'A' and content[i+3][j+3] == 'S':
            xmas_count += 1
        if content[i][j] == 'S' and content[i+1][j+1] == 'A' and content[i+2][j+2] == 'M' and content[i+3][j+3] == 'X':
            xmas_count += 1

#átlós ellenőrzés  / jobbra fel
for i in range(len(content) - 3):
    for j in range(3, len(content[i])):
        if content[i][j] == 'X' and content[i+1][j-1] == 'M' and content[i+2][j-2] == 'A' and content[i+3][j-3] == 'S':
            xmas_count += 1
        if content[i][j] == 'S' and content[i+1][j-1] == 'A' and content[i+2][j-2] == 'M' and content[i+3][j-3] == 'X':
            xmas_count += 1
"""

for i in range(1, len(content) - 1):
    for j in range(1, len(content[i]) - 1):
        if ((content[i-1][j-1] == 'M' and content[i][j] == 'A' and content[i+1][j+1] == 'S') or (content[i-1][j-1] == 'S' and content[i][j] == 'A' and content[i+1][j+1] == 'M')) and ((content[i-1][j+1] == 'M' and content[i][j] == 'A' and content[i+1][j-1] == 'S') or (content[i-1][j+1] == 'S' and content[i][j] == 'A' and content[i+1][j-1] == 'M')):
            xmas_count += 1

print(xmas_count)