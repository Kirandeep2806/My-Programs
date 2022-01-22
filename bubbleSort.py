def bubbleSort(arr):
    for i in range(len(arr)):
        swapCount = 0
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapCount += 1
        if not swapCount:
            return arr
    return arr


arr = list(map(int, input("Enter the numbers : ").split()))
sorted_arr =  bubbleSort(arr)

print("Sorted array :", sorted_arr)