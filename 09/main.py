file = open('input.txt', 'r')
content = file.read()

disk_data = []
for char in content:
    disk_data.append(char)
"""
EZ ITT A 9A MEGOLDÁS
"""
# először dekódolnunk kell az adatot a fájl-szóköz-fájl-szóköz szabály alapján
# két segédlista a B feladathoz: fájlméretek és szóközméretek, illetve szóköz-indexek
decoded_data = []
file_sizes = []
space_sizes = []
space_indices = []
space_indices_helper = 0
for i in range(len(disk_data)):
    # mivel az első szám fájl, ezért ha i páros, fájlról van szó, ha i páratlan, szóközökről
    if (i % 2) == 0:
        # annyi darab fájlt kell beírni, ahányas szám szerepel a kódolatlan adatban
        # a beírandó id pedig mindig i/2 lesz, tehát
        for x in range(int(disk_data[i])):
            decoded_data.append(round(i/2))
        file_sizes.append(int(disk_data[i]))
    else:
        #annyi darab szóköz, ahányas a szám, ismét
        for x in range(int(disk_data[i])):
            decoded_data.append('.')
        space_sizes.append(int(disk_data[i]))
        space_indices.append(space_indices_helper)
    space_indices_helper += int(disk_data[i])


# # elkezdjük a tömörítést

# # amíg van szóköz a listában, addig kell futnia a cserélgetésnek
# while '.' in decoded_data:

#     # megkeressük a legutolsó olyan elem _indexét_, ami nem szóköz
#     for i in range(len(decoded_data)-1, 0, -1):
#         if decoded_data[i] != '.':
#             index_of_item_to_remove = i
#             break
#         # ha pedig szóköz van a végén, akkor azt kitöröljük
#         else:
#             decoded_data.pop(i)

#     # megkeressük az első szóköz _indexét_
#     for i in range(len(decoded_data)):
#         if decoded_data[i] == '.':
#             index_of_first_space = i
#             break


#     # áthelyezzük az utolsó elemet a szóköz helyére
#     decoded_data[index_of_first_space] = decoded_data[index_of_item_to_remove]
#     decoded_data.pop(index_of_item_to_remove)

"""
EZ MEG A 9B
"""

# print(decoded_data)
# print(file_sizes)
# print(space_sizes)
# print(space_indices)
# a fájlokon kell végigmenni, és azokat _pontosan egyszer_ megpróbálni áthelyezni; tehát mindenképpen a fájlokon kell végigiterálnunk - hátulról előre
# mi a legnagyobb fájl ID?
max_file_id = decoded_data[-1]

for current_file_id in range(max_file_id, 0, -1):
    # az aktuálisan vizsgált fájl méretét ki tudjuk nyerni a file_sizes listából
    current_file_size = file_sizes[current_file_id]
    # meg kell néznünk a space_sizes listában, hogy létezik-e akkora hely, ahova át tudjuk helyezni a fájlt
    index_of_space_to_use = -1
    for i in range(len(space_sizes)):
        if space_sizes[i] >= current_file_size:
            # ha van ilyen hely, akkor meg kell keresnünk az indexét
            index_of_space_to_use = space_indices[i]
            space_helper_index = i
            break
    # ha találtunk megfelelő helyet, akkor azt is ellenőriznünk kell, hogy ez balra van-e a fájl eredeti helyétől
    if index_of_space_to_use != -1 and decoded_data.index(current_file_id) > space_indices[i]:
        # a fájl eredeti helyére szóközöket írunk
        while current_file_id in decoded_data:
            decoded_data[decoded_data.index(current_file_id)] = '.'
        for x in range(current_file_size):
            decoded_data[index_of_space_to_use + x] = current_file_id
        space_sizes[space_helper_index] -= current_file_size
        space_indices[space_helper_index] += current_file_size
   


# a checksum kiszámolásához újra végigmegyünk a listán
checksum = 0
for i in range(len(decoded_data)):
    if decoded_data[i] != '.':
        checksum += int(decoded_data[i])*i
    # print(checksum)
print(checksum)