import itertools

operators = ['+', '*', '||']

file = open('input.txt', 'r')
raw_content = file.readlines()
content = []
# sorvégjelek törlése
for item in raw_content:
    content.append(item.replace("\n", ""))


sum = 0
for item in content:
    # első lépésben szét kell szednünk az input sort várt eredményre és operandusokra
    result, operands = item.split(":")
    list_of_operands = operands.split()

    result = int(result)
    # az operandusok száma megadja, hogy hány kombinációra van szükségünk az operátorokból
    number_of_combinations = len(list_of_operands) - 1

    # elkészítjük a kombinációkat
    operator_combinations = list(itertools.product(operators, repeat=number_of_combinations))



    # végigmegyünk az előbb előállított operátor-kombinációkon
    for i in range(len(operator_combinations)):
        current_result = int(list_of_operands[0])
        # végigmegyünk az i. operator kombináción lépésenként
        for j in range(len(operator_combinations[i])):
            if operator_combinations[i][j] == '+':
                current_result = current_result + int(list_of_operands[j+1])
            elif operator_combinations[i][j] == '*':
                current_result = current_result * int(list_of_operands[j+1])
            elif operator_combinations[i][j] == '||':
                current_result = int(str(current_result) + list_of_operands[j+1])

        if result == current_result:
            sum += result
            print('Current result is ', current_result, 'expected result is ', result)
            break    

            
        #     print(current_result)

        #     current_combination = list(operator_combinations[0])
        #     print(current_combination)
        #     while found == False and len(list_of_operands) > 0:
        #         next_operand = int(list_of_operands.pop(0))
        #         print(next_operand)
        #         next_operator = current_combination.pop(0)
        #         print(next_operator)
        #         if next_operator == '+':
        #             current_result = current_result + next_operand
        #         elif next_operator == '*':
        #             current_result = current_result * next_operand
        #         if result == current_result:
        #             found == True
        #             sum += result
        #             print('Current result is ', current_result, 'expected result is ', result)

print(sum)
