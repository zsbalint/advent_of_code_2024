import copy

# megnézzük, hogy a _map_ térképen az _x_, _y_ pozícióban lévő mező _direction_ szomszédja _value_-e, ha igen, visszaadjuk a koordinátáit
def check_neighbor(map, y, x, direction, value):
    match direction:
        case 'N':
            if (y > 0) and (map[y-1][x] == str(value)):
                return [y-1, x]
            else:
                return [-1, -1]
        case 'E':
            if x < len(map[0]) - 1 and map[y][x+1] == str(value):
                return [y, x+1]
            else:
                return [-1, -1]
        case 'S':
            if y < len(map) - 1 and map[y+1][x] == str(value):
                return [y+1, x]
            else:
                return [-1, -1]
        case 'W':
            if x > 0 and map[y][x-1] == str(value):
                return [y, x-1]
            else:
                return [-1, -1]


file = open('input.txt', 'r')
raw_content = file.readlines()
map = []
# sorvégjelek törlése
for item in raw_content:
    map.append(item.replace("\n", ""))

# keressük meg az összes trailheadet
trailheads = []
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == '0':
            trailheads.append([y,x])

dummy_dictionary = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

result = 0

for trailhead in trailheads:
    # kell egy dictionary az aktuális trailheadnek
    curr_dict = copy.deepcopy(dummy_dictionary)
    curr_dict[0].append(trailhead)
    
    for i in range(9):
        for j in range(len(curr_dict[i])):
            # megnézzük, hogy az i. elem szomszédai között van-e, ami i+1 értékű, ha igen, felvesszük a dictionary-be
            # print(curr_dict[i][j][0], curr_dict[i][j][1])
            [north_y, north_x] = check_neighbor(map, curr_dict[i][j][0], curr_dict[i][j][1], 'N', i+1)
            if [north_y, north_x] != [-1, -1] and any([north_y, north_x] in sublist for sublist in curr_dict.values()) == False:
                curr_dict[i+1].append([north_y, north_x])
            [east_y, east_x] = check_neighbor(map, curr_dict[i][j][0], curr_dict[i][j][1], 'E', i+1)
            if [east_y, east_x] != [-1, -1] and any([east_y, east_x] in sublist for sublist in curr_dict.values()) == False:
                curr_dict[i+1].append([east_y,east_x])
            [south_y, south_x] = check_neighbor(map, curr_dict[i][j][0], curr_dict[i][j][1], 'S', i+1)
            if [south_y, south_x] != [-1, -1] and any([south_y, south_x] in sublist for sublist in curr_dict.values()) == False:
                curr_dict[i+1].append([south_y, south_x])
            [west_y, west_x] = check_neighbor(map, curr_dict[i][j][0], curr_dict[i][j][1], 'W', i+1)
            if [west_y, west_x] != [-1, -1] and any([west_y, west_x] in sublist for sublist in curr_dict.values()) == False:
                curr_dict[i+1].append([west_y, west_x])

    # összegyűjtöttük az adott trailheadből bejárható összes pontot; meg kell számolnunk a 9eseket
    result += (len(curr_dict[9]))


print(result)
