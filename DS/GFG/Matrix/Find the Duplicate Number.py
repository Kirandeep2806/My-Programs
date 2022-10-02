#!/usr/bin/python3

nums = list(map(int, input().split()))

while nums[0]!=nums[nums[0]]:
    temp = nums[0]
    nums[0] = nums[temp]
    nums[temp] = temp

print(nums[0])
