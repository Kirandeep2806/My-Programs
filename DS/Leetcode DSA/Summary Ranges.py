class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        res = []
        cnt = 0
        if n == 0:
            return []
        if n == 1:
            return [str(nums[0])]
        if n == 2:
            if nums[1]==nums[0]+1:
                return [f"{nums[0]}->{nums[1]}"]
            return list(map(str,nums))
        s = str(nums[0])
        for i in range(n):
            if i == n-1:
                print(s)
                if nums[n-1]==nums[n-2]+1:
                    s += "->" + str(nums[n-1])
                    res.append(s)
                else:
                    if cnt > 0:
                        s += "->" + str(nums[n-2])
                        res += [s, nums[n-1]]
                    else:
                        res.append(str(nums[n-1]))
            else:
                if nums[i+1]==nums[i]+1:
                    # if cnt==0:
                        # s += str(nums[i])
                    cnt += 1
                else:
                    if cnt > 0:
                        s += "->" + str(nums[i])
                    res.append(s)
                    cnt = 0
                    s = str(nums[i+1])
        return res