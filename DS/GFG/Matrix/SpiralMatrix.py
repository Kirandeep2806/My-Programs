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
    tempLeft = left
    while(tempLeft <= right):
        print(l[top][tempLeft], end=" ")
        tempLeft += 1
    top += 1
    tempTop = top
    while(tempTop <= bottom):
        print(l[tempTop][right], end=" ")
        tempTop += 1
    right -= 1
    if(top <= bottom):
        tempRight = right
        while(tempRight >= left):
            print(l[bottom][tempRight], end=" ")
            tempRight -= 1
        bottom -= 1
    if(left <= right):
        tempBottom = bottom
        while(tempBottom >= top):
            print(l[tempBottom][left], end=" ")
            tempBottom -= 1
        left += 1
