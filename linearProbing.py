import numpy as np

l_size = int(input("Enter the size of the list : "))
elements = list(map(int, input("Enter the data as space separated inputs : ").split()))

arr = np.array([None]*l_size, dtype=object)
i = 0
ptr = 0

while ptr < elements.__len__():
    index = (elements[ptr]+i) % l_size
    if arr[index] is None:
        arr[index] = elements[ptr]
        ptr += 1
        i = 0
    else:
        i += 1
    if i == l_size:
        print("Can't store data from index {} as memory overflows!!".format(ptr))
        break

print("After linear probing the data in array is : ", arr)

key = int(input("Enter the element to be searched : "))
i = 0

while i<len(elements):
    index = (key+i)%l_size
    if arr[index] == key:
        print("Found at index {}".format(index))
        break
    else:
        i += 1

else:
    print("Element not found!!")
