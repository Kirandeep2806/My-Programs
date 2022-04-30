arr = list(map(int, input("Enter the input with the space separated values : ").split()))
sumOfFrequencyCount = [0]*10
for i in range(len(arr)):
    sumOfFrequencyCount[arr[i]] += 1

for i in range(1, 10):
    sumOfFrequencyCount[i] += sumOfFrequencyCount[i-1]

res =  [0]*len(arr)
for i in arr:
    sumOfFrequencyCount[i] -= 1
    res[sumOfFrequencyCount[i]] = i

print("Sorted digits :", res)