#!/usr/bin/python3

# l = [[1,2,3], [4,5,6], [7,8,9]]
l = [[1,2,3,4],[5,6,7,8], [9,10,11,12]]
# l = [[1,2,3,4]]
r = l.__len__()
c = l[0].__len__()

top = 0
right = c-1
bottom =  r-1
left = 0

# top and bottom handles rows
# left and right handles columns

# 1 2 3
# 4 5 6
# 7 8 9

# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

while(top<=bottom and left<=right):
    tempTop = left
    while(tempTop <= right):
        print(l[top][tempTop], end=" ")
        tempTop += 1
    top += 1
    tempRight = top
    while(tempRight <= bottom):
        print(l[tempRight][right], end=" ")
        tempRight += 1
    right -= 1
    tempBottom = right
    while(tempBottom >= left):
        print(l[bottom][tempBottom], end=" ")
        tempBottom -= 1
    bottom -= 1
    tempLeft = bottom
    while(tempLeft >= top):
        print(l[tempLeft][left], end=" ")
        tempLeft -= 1
    left += 1
    print()


