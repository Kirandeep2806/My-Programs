import sys

input = input().split(" ")
print(input)
valueDict = {"R":3,"B":2,"G":1}

if valueDict[input[0]] > valueDict[input[1]]:
    sys.stdout.write(input[0])
else:
    sys.stdout.write(input[1])
