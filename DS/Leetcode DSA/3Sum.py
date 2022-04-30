#!/usr/bin/python3

from collections import defaultdict, Counter

nums = [12,0,3,-14,5,-11,11,-5,-2,-1,6,-7,-10,1,4,1,1,9,-3,6,-15,0,6,1,6,-12,3,7,11,-6,-8,0,9,3,-7,-1,7,-10,1,13,-4,-7,-9,-7,9,3,1,-13,-3,13,8,-11,-9,-8,-3,4,-13,7,-11,5,-14,-4,-9,10,6,-9,-6,-9,-12,11,-11,-9,11,-5,0,-3,13,-14,-1,-13,7,-7,14,5,0,-4,-6,-6,-11,-2,14,-10,2,12,8,-7,-11,-13,-9,14,5,-5,-9,1,-2,6,5,-12,-1,-10,-9,-9,-10,12,11]

# nums = list(map(int, input().split()))
res = []

tracker = defaultdict(lambda: 0)
# print(tracker[10])
for i in nums:
    tracker[i] += 1

# print(tracker)

l = len(nums)
done = defaultdict(lambda: 0)
doneTracker = []

for i in range(l):
    tracker[nums[i]] -= 1
    if not done[nums[i]]:
        for j in range(i+1, l):
            thirdVal = 0-nums[i]-nums[j]
            tracker[nums[j]] -= 1
            # print(tracker, nums[i], nums[j])
            c = Counter([nums[i], nums[j], thirdVal])
            if c in doneTracker:
                tracker[nums[j]] += 1
                continue
            if tracker[thirdVal]:
                res.append([nums[i], nums[j], thirdVal])
                doneTracker.append(c)
            tracker[nums[j]] += 1
        done[nums[i]] = 1
    tracker[nums[i]] += 1

print(res)
