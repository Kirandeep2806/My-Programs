#!/usr/bin/python3

for i in range(int(input())):
    numbers = []
    operators = [0, 0]
    n = int(input())
    expr = input()
    for i in expr:
        if i.isdigit():
            numbers.append(i)
        else:
            if i == '+':
                operators[0] += 1
            else:
                operators[1] += 1
    numbers.sort(reverse=True)
    allOperatorCount = sum(operators)
    startInserting = n-2*allOperatorCount
    for i in range(numbers.__len__()):
        if i >= startInserting and operators[0]!=0:
            print(f"+{numbers[i]}", end="")
            operators[0] -= 1
        elif i >= startInserting and operators[1]!=0:
            print(f"-{numbers[i]}", end="")
            operators[1] -= 1
        else:
            print(numbers[i], end="")
    print()
