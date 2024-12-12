import time
import bigtree

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


    while finished == False:
        
        # search for the deepest unprocessed node
        available_nodes = bigtree.findall(root, lambda node: node.processed == False)
        deepest = 0
        for node in available_nodes:
            if node.depth > deepest:
                deepest = node.depth
        current_node = bigtree.findall(root, lambda node: (node.depth == deepest and node.processed == False))[0]
        # print("Iteration", iter, "Current node:", current_node.name)
        if current_node.depth == max_depth+1:
            total_stones += 1
            # bigtree.print_tree(root)
            # print("Starting number {0} has reached maximum depth with a result of {1} in {2} seconds".format(number, current_node.value, time.time()-start))
            bigtree.shift_nodes(root, [current_node.path_name], [None])
            # bigtree.print_tree(root)
            # break
        else:
            children_list = step(current_node.value)
            for children in children_list:
                child = bigtree.Node(str(id), value = children, processed = False, parent = current_node)
                id += 1
                current_node.processed = True
                # print("Child node", child.value, "is now added under", current_node.value)
        # cleanup: search for every node that has 0 children and processed == True
        to_delete = bigtree.findall(root, lambda node: (len(node.children) == 0 and node.processed == True))
        for item in to_delete:
            # print("Node with value", item.value, "depth", item.depth, "is deleted at", time.time() - start, "seconds.") 
            bigtree.shift_nodes(root, [item.path_name], [None])
        
        if len(bigtree.findall(root, lambda node: node.processed == False)) == 0:
            finished = True 

    return total_stones    


final_sum = 0
for i in stones:
    result = process_number(i,BLINKS)
    print("Number {0} has finished with a result of {1} in {2} seconds.".format(i, result, time.time()-start))
    final_sum += result
# process_number('125', 25)
# process_number('17', 25)

print(final_sum)