l = list(map(int, input("Enter list of numbers : ").split()))
find = int(input("Enter the element to be found : "))

def binarySearch(arr, find, low, high):
    if high >= low:
        mid = (low + high)//2
        if arr[mid] > find:
            return binarySearch(arr, find, low, mid-1)
        elif arr[mid] < find:
            return binarySearch(arr, find, mid+1, high)
        else:
            return mid
    else:
        return -1

print(binarySearch(l, find, 0, len(l)-1))