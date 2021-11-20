l = list(map(int, input("Enter list of numbers : ").split()))
find = int(input("Enter the element to be found : "))

def binarySearch(l, find):
    low = 0
    high = len(l) - 1
    mid = 0
    while low <= high:
        mid = (low + high)//2
        if l[mid] < find:
            low = mid + 1
        elif l[mid] > find:
            high = mid - 1
        else:
            return mid
    return -1

print(binarySearch(l, find))