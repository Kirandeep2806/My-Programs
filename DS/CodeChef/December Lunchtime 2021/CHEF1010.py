for i in range(int(input())):
    digitLen = int(input())
    oneCount = zeroCount = 0
    digit = int(input(), base=2)
    while digit != 0:
        if digit & 1:
            oneCount += 1
        else:
            zeroCount += 1
        digit >>= 1
    if oneCount == zeroCount:
        print(oneCount - 1)
    elif zeroCount >= oneCount >= 2 and  zeroCount > oneCount:
        print(oneCount)
    elif zeroCount >= oneCount >= 2 and oneCount > zeroCount:
        pass
