import sys
import functools


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

a fastruktúrás megoldás lefutása 7500 évet venne igénybe. köszi.



file = open('input.txt', 'r')
content = file.read()
stones = content.split()

def step(number):
    if number == '0':
        return ['1']
    elif len(number) % 2 == 0:
        s1 = number[:int(len(number)/2)]
        s2 = number[int(len(number)/2):]
        return [s1, str(int(s2))]
    else:
        return [str(int(number)*2024)]
       
    


def process_number(number, max_depth):
    id = 0
    total_stones = 0
    # creating the root node
    root = bigtree.Node(str(id), value = number, processed = False)
    id += 1
    # run until done
    finished = False

    current_node = root
    while finished == False:
        # ha elértük a legalsó szintet, számolunk és törlünk
        if current_node.depth == max_depth+1:
            total_stones += 1
            # bigtree.print_tree(root)
            # print("Starting number {0} has reached maximum depth with a result of {1} in {2} seconds".format(number, current_node.value, time.time()-start))
            if len(current_node.siblings) > 0:
                next_node = current_node.siblings[0]
            else:
                next_node = current_node.parent
            bigtree.shift_nodes(root, [current_node.path_name], [None])
            current_node = next_node
            # bigtree.print_tree(root)
            # break
        elif len(current_node.children) == 0 and current_node.processed == True:
            if len(current_node.siblings) > 0:
                next_node = current_node.siblings[0]
            else:
                next_node = current_node.parent
            # print("Deleting childless processed node with value {0} and depth {1} at {2} seconds.".format(current_node.value, current_node.depth, time.time()-start))
            bigtree.shift_nodes(root, [current_node.path_name], [None])
            current_node = next_node       
        else:
            children_list = step(current_node.value)
            for children in children_list:
                child = bigtree.Node(str(id), value = children, processed = False, parent = current_node)
                next_node = child
                id += 1
                current_node.processed = True
                # print("Child node", child.value, "is now added under", current_node.value)
            current_node = next_node
        
        if current_node == root:
            finished = True 
    # print("Number {0} has finished with a result of {1} in {2} seconds.".format(number, total_stones, time.time()-start))
    return total_stones    
"""



# Read the raw example/input text
with open("input.txt", "r") as input_file:
    raw_text = input_file.read()

# Parse text into indvidual
stones = list(map(int, raw_text.split()))

# @functools.lru_cache(maxsize=None)
def single_blink_stone(value):

    # Convert value to text
    text = str(value)

    # Count the digits in the number
    num_of_digits = len(text)
    
    # Zeros get updated to ones first
    if value == 0:
        return (1, None)

    # Even number of digits get split into two stones
    elif num_of_digits % 2 == 0:
        mid_point = num_of_digits // 2
        left_stone = int(text[:mid_point])
        right_stone = int(text[mid_point:])

        return (left_stone, right_stone)
    
    else:
        return (value * 2024, None)

# @functools.lru_cache(maxsize=None)
def count_stone_blinks(stone, depth):

    # For this iteration, what is the update for this stone?
    left_stone, right_stone = single_blink_stone(stone)

    # Is this the final iteration
    if depth == 1:

        # Final iteration, just count if have one or two stones
        if right_stone is None:
            return 1
        else:
            return 2

    else:

        # Recurse to the next level and add the results if there
        # are two stones
        output = count_stone_blinks(left_stone, depth - 1)
        if right_stone is not None:
            output += count_stone_blinks(right_stone, depth - 1)
        
        return output

def run(count):

    # Keep are running count of the overall output
    output = 0

    # Look at each stone
    for stone in stones:

        # Add up how many stones each one turns into
        output += count_stone_blinks(stone, count)

    return output

print()
print("Part 1")
print(run(25))

print()
print("Part 2")
print(run(75))



