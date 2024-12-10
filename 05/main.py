file = open('input.txt', 'r')
content = file.readlines()


sum = 0


def check_if_correct(order):
        # az orderben lévő összes lehetséges oldalszám-párosítást össze kell vetni a szabályokkal
    order_is_correct = True
    for i in range(len(order)):
        for j in range(i+1, len(order)):
            # szabályokkal történő összevetés: ha az elsőként (i) vizsgált oldal valamelyik szabályban a másodikként (j) vizsgált oldal _után_ helyezkedik el, akkor hibát találtunk
            if [order[j], order[i]] in rules:
                order_is_correct = False
    return order_is_correct

# válogassuk szét az inputot rules és printing_orders listákba
rules = []
printing_orders = []


rules_to_list = True
for item in content:
    if item == '\n':
        rules_to_list = False
    else:
        if rules_to_list:
            current_item = item.replace('\n', '')
            a,b = current_item.split('|')
            rules.append([a,b])
        else:
            current_item = item.replace('\n', '')
            items_to_add = current_item.split(',')
            printing_orders.append(items_to_add)



correct_orders = []
incorrect_orders = []

# végig kell mennünk az összes printing orderen, és mindegyiknél leellenőrizni a validitásukat
for order in printing_orders:
    # if order_is_correct:
    #     sum += int(order[len(order) // 2])
    if check_if_correct(order):
        correct_orders.append(order)
    else:
        incorrect_orders.append(order)


# és akkor most rendbe kell rakni a hibás odereket valahogy...
for order in incorrect_orders:
    # gyűjtsük ki a kapcsolódó szabályokat az adott orderhez
    rules_to_apply = []
    for i in range(len(order)):
        for j in range(len(rules)):
            if rules[j][0] in order and rules[j][1] in order:
                if [rules[j][0], rules[j][1]] not in rules_to_apply:
                    rules_to_apply.append(rules[j])

    # kigyűjtöttük. most kell ebből szabályokat alkalmazni.
    # végigmegyünk az alkalmazandó szabályokon, és ha hibába ütközünk, megcseréljük a lista elemeit
    while check_if_correct(order) is False:
        for rule in rules_to_apply:
            # megkeressük, hogy a vizsgált szabályban szereplő elemek hol vannak az orderben
            if order.index(rule[0]) > order.index(rule[1]):
                order[order.index(rule[0])], order[order.index(rule[1])] = order[order.index(rule[1])], order[order.index(rule[0])]

    
    # print (corrected_order)



for order in incorrect_orders:
    sum += int(order[len(order) // 2])
print(sum)