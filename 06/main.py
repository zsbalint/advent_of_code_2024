import time
import copy

def solve_the_map(map, first = False):
    # hány lépés után tekintjük úgy, hogy végtelen ciklusba keveredtünk?
    LIMIT = 1000000
    visited_fields = copy.deepcopy(map)
    # meg kell keresnünk a csicska kezdőpozícióját 
    pos_x = -1
    pos_y = -1
    direction = 'N'
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "^":
                pos_x = x
                pos_y = y

    # addig kell pörgetni a dolgot, amíg a határra nem érünk, tehát kell irány változó, határraérés változó, és a különböző állapotok miatt kell mozgás/fordulás változó is 
    reached_exit = False
    tries = 0
    stuck = False
    action = 'move'
    while reached_exit == False and stuck == False:
        # először ellenőrizzük, hogy a következő lépésben mi fog történni
        match direction:
            case 'N':
                if pos_y == 0:
                    reached_exit = True
                    visited_fields[pos_y][pos_x] = 'X'
                elif map[pos_y - 1][pos_x] == '#':
                    action = 'turn'
                elif map[pos_y -1][pos_x] == '.':
                    action = 'move'
            case 'E':
                if pos_x == len(map[0]) - 1:
                    reached_exit = True
                    visited_fields[pos_y][pos_x] = 'X'
                elif map[pos_y][pos_x + 1] == '#':
                    action = 'turn'
                elif map[pos_y][pos_x + 1] == '.':
                    action = 'move'
            case 'S':
                if pos_y == len(map) - 1:
                    reached_exit = True
                    visited_fields[pos_y][pos_x] = 'X'
                elif map[pos_y + 1][pos_x] == '#':
                    action = 'turn'
                elif map[pos_y + 1][pos_x] == '.':
                    action = 'move'
            case 'W':
                if pos_x == 0:
                    reached_exit = True
                    visited_fields[pos_y][pos_x] = 'X'
                elif map[pos_y][pos_x - 1] == '#':
                    action = 'turn'
                elif map[pos_y][pos_x - 1] == '.':
                    action = 'move'
        # majd végrehajtjuk a kiválasztott akciót, ha még nem a pálya szélén vagyunk
        if reached_exit == False:
            match direction:
                case 'N':
                    if action == 'move':
                        visited_fields[pos_y][pos_x] = 'X'
                        pos_y -= 1
                    if action == 'turn':
                        direction = 'E'
                case 'E':
                    if action == 'move':
                        visited_fields[pos_y][pos_x] = 'X'
                        pos_x += 1
                    if action == 'turn':
                        direction = 'S'
                case 'S':
                    if action == 'move':
                        visited_fields[pos_y][pos_x] = 'X'
                        pos_y += 1
                    if action == 'turn':
                        direction = 'W'
                case 'W':  
                    if action == 'move':
                        visited_fields[pos_y][pos_x] = 'X'
                        pos_x -= 1
                    if action == 'turn':
                        direction = 'N'
        
        tries += 1
        if tries > LIMIT:
            stuck = True
            print("The guard is caught in a loop!")
            return 1
        if reached_exit and first:
            return visited_fields
        elif reached_exit and first == False:
            print("The guard exited succesfully!")
            return 0
        # for i in range(len(map_visited_fields)):
        #     print(i, map_visited_fields[i])
        # time.sleep(0.05)
        # print(action, direction, pos_x, pos_y)

        # if pos_x == 47 and pos_y == 61:
        #     for i in range(55, 65):
        #             print(map[i][42:52])



file = open('input.txt', 'r')
raw_content = file.readlines()
file.close()

shitty_map = []
map = []
visited_fields = []
for item in raw_content:
    shitty_map.append(item.replace("\n", ""))

for row in shitty_map:
    row_to_add = []
    for char in row:
        row_to_add.append(char)
    map.append(row_to_add)


first_run = solve_the_map(map, first = True)
first_run_result = copy.deepcopy(first_run)
for y in range(len(first_run_result)):
    print(first_run_result[y])


looped = 0
for y in range(len(first_run_result)):
    for x in range(len(first_run_result[y])):
        if first_run_result[y][x] == 'X':
            new_map_to_check = copy.deepcopy(map)
            new_map_to_check[y][x] = "#"
            print("Trying the map where {}, {} is changed:".format(x, y))
            looped += solve_the_map(new_map_to_check)

print(looped)



# print("")



# sum = 0
# for y in range(len(visited_fields)):
#     for x in range(len(visited_fields[y])):
#         if visited_fields[y][x] == 'X':
#             sum += 1
# print(sum)