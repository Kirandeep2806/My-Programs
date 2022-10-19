#User function Template for python3

def LargButMinFreq(arr,n):
    hashmap = {}
    for i in arr:
        if not hashmap.get(i, 0):
            hashmap[i] = 0
        hashmap[i] += 1
    min_freq = 100000
    for key in hashmap:
        if hashmap[key] < min_freq:
            min_freq = hashmap[key]
    max_val = 0
    for key in hashmap:
        if hashmap[key] == min_freq and key > max_val:
            max_val = key
    return max_val
    

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends
