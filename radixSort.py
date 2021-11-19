arr = list(map(int, input("Enter the input with the space separated values : ").split()))
divisor = 1

for _ in range(len(str(max(arr)))):
    bucket = [[] for _ in range(10)]
    for ele in arr:
        lsd = (ele//divisor)%10
        bucket[lsd].append(ele)
    arr.clear()
    for nestedList in bucket:
        for ele in nestedList:
            arr.append(ele)
    divisor *= 10

print("Sorted array :", *arr)