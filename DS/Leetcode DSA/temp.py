for _ in range(int(input())):
    n,target=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    cnt=0
    left, right, runSum, count = 0, 0, 0, 0
    while right < n:
        runSum += arr[right]
        while runSum > target:
            runSum -= arr[left]
            left += 1
        count += right - left + 1
        right += 1
    print(count)
