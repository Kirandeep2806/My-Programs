# https://www.codechef.com/INFI21C/problems/MARBLE

n = int(input())
vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
for i in range(n):
    length = int(input())
    l = []
    for j in range(2):
        l.append(input())
    steps = 0
    for j in range(length):
        if l[1][j] == l[0][j]:
            pass
        elif (vowels.get(l[1][j], 0) and vowels.get(l[0][j], 0)) or ((not(vowels.get(l[1][j], 0))) and (not(vowels.get(l[0][j], 0)))):
            steps += 2
        elif vowels.get(l[1][j], 0) or vowels.get(l[0][j], 0):
            steps += 1
        else:
            steps += 0

    print(steps)