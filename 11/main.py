import copy

file = open('input.txt', 'r')
content = file.read()
stones = content.split()
new_stones = []
BLINKS = 25

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
    # print("Blink", blink+1, "stones:", stones)
# print(stones)
print(len(stones))