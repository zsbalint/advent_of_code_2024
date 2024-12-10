import itertools
import copy


file = open('input.txt', 'r')
raw_content = file.readlines()
file.close()

shitty_map = []
map = []
for item in raw_content:
    shitty_map.append(item.replace("\n", ""))

for row in shitty_map:
    row_to_add = []
    for char in row:
        row_to_add.append(char)
    map.append(row_to_add)

map_height = len(map)
map_width = len(map[0])

# készítünk egy másodlagos térképet, amelyen ábrázoljuk az antinode-ok helyét
antinode_map = []
for i in range(map_height):
    empty_map_row = []
    for j in range(map_width):
        empty_map_row.append('.')
    antinode_map.append(empty_map_row)

# megkeressük az összes előforduló betűt a térképen
letters = []
for row in map:
    for char in row:
        if char != '.' and char not in letters:
            letters.append(char)

# végigmegyünk a betűkön
for letter in letters:
    # megkeressük az adott betű összes előfordulását
    locations = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == letter:
                locations.append([x, y])
    # létrehozzuk az összes vizsgálandó párosítást
    pairs_to_check = list(itertools.combinations(locations, 2))
    
    # minden párt vizsgálni kell, két irányba, hogy az adott lokáció megfelelő-e vagy nem
    for pair in pairs_to_check:
        # a két antenna távolsága:
        dist_x = abs(pair[0][0] - pair[1][0])
        dist_y = abs(pair[0][1] - pair[1][1])

        # a b feladatrész miatt be kell tenni az egész vizsgálatot egy ciklusba, hogy több antinode-ot találjunk egyenlő távolságokra. lehetne okosan, de én buta vagyok: megkeresem azt a számot, ami az x és y közül a kisebb, és annak
        # használatával definiálom a ciklus futások számát
        number_of_tries = max(map_width//dist_x, map_height//dist_y)
        for i in range(1, number_of_tries):
        # ha a vizsgált szám a kisebb, akkor kivonjuk belőle a különbséget. ha a nagyobb, akkor hozzáadjuk. egyenlő esetén értelemszerűen nem változik
            if pair[0][0] < pair[1][0]:
                res1x = pair[0][0] - dist_x*i
                res2x = pair[1][0] + dist_x*i
            elif pair[0][0] > pair[1][0]:
                res1x = pair[0][0] + dist_x*i
                res2x = pair[1][0] - dist_x*i
            else:
                res1x = pair[0][0]
                res2x = pair[0][0]
            if pair[0][1] < pair[1][1]:
                res1y = pair[0][1] - dist_y*i
                res2y = pair[1][1] + dist_y*i
            elif pair[0][1] > pair[1][1]:
                res1y = pair[0][1] + dist_y*i
                res2y = pair[1][1] - dist_y*i
            else:
                res1y = pair[0][1]
                res2y = pair[0][1]
            # print(pair, res1x, res1y, res2x, res2y)

            # megvannak a párhoz tartozó pontok, ellenőrizzük, hogy elférnek-e a térképen. ha igen, berajzoljuk
            if 0 <= res1x < map_width and 0 <= res1y < map_height:
                antinode_map[res1y][res1x] = '#'
            if 0 <= res2x < map_width and 0 <= res2y < map_height:
                antinode_map[res2y][res2x] = '#'

        # ezt követően pedig minden egyes antenna lokációt is be kell jelölnünk a térképen
        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[y][x] != '.':
                    antinode_map[y][x] = '#'

result = 0
for row in antinode_map:
    result += row.count('#')

print(result)