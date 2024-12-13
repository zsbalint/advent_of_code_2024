import time
import bigtree
import functools
import copy

start = time.time()


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

"""

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







final_sum = 0
for i in stones_input:
    first = process_number(tuple([i]),)
    result = process_number(tuple(first),BLINKS)
    print("Number {0} has finished with a result of {1} in {2} seconds.".format(i, len(result), time.time()-start))
    final_sum += len(result)
print(final_sum)
print(process_number.cache_info())



