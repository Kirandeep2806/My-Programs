l = list(map(int, input("Enter numbers : ").split()))
n = int(input("Enter the element to be searched : "))

def linearSearch(element, position, arr):
    if arr[position] == element:
        return position
    if len(arr) == position + 1:
        return "Element not found!"
    return linearSearch(element, position+1, arr)


if type(acknowledge:=linearSearch(n, 0, l)).__name__ == "int":
    print(f"Found at index {acknowledge}")
else:
    print(acknowledge)
