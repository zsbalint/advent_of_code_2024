import copy
import time

start = time.time()

BLINKS = 25
"""
11A
"""
"""
file = open('input.txt', 'r')
content = file.read()
stones = content.split()
new_stones = []

for blink in range(BLINKS):
    new_stones.clear()
    for i in range(len(stones)):
        # print(i)
        # print(stones[i])
        if stones[i] == '0':
            new_stones.append('1')
        elif len(stones[i]) % 2 == 0:
            s1 = stones[i][:int(len(stones[i])/2)]
            s2 = stones[i][int(len(stones[i])/2):]
            new_stones.append(s1)
            new_stones.append(str(int(s2)))
            # print(s1, s2)
        else:
            new_stones.append(str(int(stones[i]) * 2024))
        # print(new_stones)
    stones = copy.deepcopy(new_stones)
    print("Blink", blink+1, "time:", time.time() - start)
# print(stones)
print(len(stones))
"""


"""
11B
"""

# átírjuk az inputot a stones1.txt fájlba, soronként egy adatot
file = open('input2.txt', 'r')
content = file.read()
stones = content.split()
file.close()
file2 = open('stones1.txt', 'w').close()
file2 = open('stones1.txt', 'a')
for i in range(len(stones)):
    if i < len(stones)-1:
        file2.write(stones[i] + '\n')
    else:
        file2.write(stones[i])
file2.close()

def get_file_length(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return len(lines)


def process_a_blink(file1, file2):
    output_file = open(file2, 'w').close()
    for i in range(get_file_length(file1)):
        input_file = open(file1, 'r')       
        output_file = open(file2, 'a')
        for n, line in enumerate(input_file):
            if n == i:
                current_stone = line
            elif n > i:
                break
        input_file.close()

        # print("Currently checked stone is", current_stone)

        current_stone = current_stone.replace('\n', '')
        if current_stone == '0':

            # print("Current stone is 0, changing to 1.")

            output_file.write('1\n')
        elif len(current_stone) % 2 == 0:
            s1 = current_stone[:int(len(current_stone)/2)]
            s2 = current_stone[int(len(current_stone)/2):]

            # print("Current stone" , current_stone, "had even digits, splitting to", s1, s2)

            output_file.write(s1 + '\n')
            output_file.write((str(int(s2))) + '\n')
            # print(s1, s2)
        else:

            # print("Else: multiply by 2024, result is", str(int(current_stone) * 2024))
            output_file.write((str(int(current_stone) * 2024)) + '\n')
        output_file.close()


for i in range(BLINKS):
    if i % 2 == 0:
        process_a_blink('stones1.txt', 'stones2.txt')
    else:
        process_a_blink('stones2.txt', 'stones1.txt')
    print("Blink", i, "finished, time:", time.time() - start) 


if BLINKS % 2 == 0:
    print(get_file_length('stones1.txt'))
else:
    print(get_file_length('stones2.txt'))