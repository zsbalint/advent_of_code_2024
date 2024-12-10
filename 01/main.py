file = open('list.txt', 'r')
content = file.readlines()


first_list = []
second_list = []


for item in content:
    a, b = item.split()
    first_list.append(int(a))
    second_list.append(int(b))    


first_list.sort()
second_list.sort()


# 01.
"""
value = 0

for i in range(len(first_list)):
    value += abs(first_list[i] - second_list[i])

print(value)
"""

# 02.
similarity_score = 0
for item in first_list:
    similarity_score += second_list.count(item) * item

print(similarity_score)