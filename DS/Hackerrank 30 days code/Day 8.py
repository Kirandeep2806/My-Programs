n = int(input())
callBook = {}
for i in range(n):
    personNumber = input().split()
    callBook[personNumber[0]] = personNumber[1]

while True:
    name = input()
    if name:
        if name in callBook:
            print(f"{name}={callBook[name]}")
        else:
            print("Not found")
    else:
        break    
n = int(input())
callBook = {}
for i in range(n):
    personNumber = input().split()
    callBook[personNumber[0]] = personNumber[1]

while True:
    try:
        name = input()
        if name in callBook:
            print(f"{name}={callBook[name]}")
        else:
            print("Not found")
    except EOFError:
        break
