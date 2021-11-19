l = list(map(int, input("Enter list of numbers : ").split()))
def selectionSort(arr, i, n):
    if i == n:
        return arr
    min = i
    for j in range(i+1, n):
        if arr[j] < arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]
    return selectionSort(arr, i+1, n)

print(selectionSort(l, 0, len(l)))