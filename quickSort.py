l = list(map(int, input("Enter number : ").split()))
n = len(l)
passCount = 0

def quickSort(l, first, last):
    global passCount
    if first<last:
        i = first
        j = last
        pivot = first
        while j > i:
            while l[i]<=l[pivot] and i<last:
                i += 1
            while l[j]>l[pivot]:
                j -= 1
            if i<j:
                l[i], l[j] = l[j], l[i]
        l[j], l[pivot] = l[pivot], l[j]
        passCount += 1
        print(f"After pass {passCount} : ", *l)
        quickSort(l, first, j-1)
        quickSort(l, j+1, last)
        
quickSort(l, 0, n-1)