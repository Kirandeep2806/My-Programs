#!/usr/bin/python3

for i in range(int(input())):
    n = int(input())
    binaryString = input()
    zeroCount = binaryString.count('0')
    oneCount = binaryString.count('1')
    if binaryString == '10':
        print(binaryString)
    else:
        print('0'*zeroCount + '1'*oneCount)
