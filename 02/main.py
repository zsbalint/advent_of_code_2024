file = open('input.txt', 'r')
content = file.readlines()

def check_if_safe(levels):
    safe = True
    # megnézzük hogy a lista növekvő vagy csökkenő
    order = ''
    if levels[0] - levels[-1] == 0:
        safe = False
    elif levels[0] - levels[-1] > 0:
        order = 'csökkenő'
    else:
        order = 'növekvő'


    for i in range(len(levels) - 1):
        if order == 'csökkenő':
            if levels[i] - levels[i+1] > 0 and levels[i] - levels[i+1] < 4:
                continue
            else:
                safe = False
        elif order == "növekvő":
            if levels[i+1] - levels[i] > 0 and levels[i+1] - levels[i] < 4:
                continue
            else:
                safe = False

    return safe


safe_count = 0
safe_levels = []
unsafe_levels = []
cleaned_safe_levels = []

for item in content:
    levels_string = item.split()
    levels = []
    for item in levels_string:
        levels.append(int(item))
    
    if check_if_safe(levels):
        safe_levels.append(levels)
    else:
        unsafe_levels.append(levels)
    
#print(len(safe_levels))

for item in unsafe_levels:
    for i in range(len(item)):
        current_try = item[:]
        current_try.pop(i)
        if check_if_safe(current_try):
            cleaned_safe_levels.append(current_try)
            break

print(len(safe_levels) + len(cleaned_safe_levels))

