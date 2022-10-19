#!/usr/bin/python3

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry=1
        for i in range(n-1, -1, -1):
            if digits[i]==9 and carry:
                digits[i]=0
            else:
                digits[i]+=1
                carry=0
                break
        else:
            digits.insert(0, 1)
        return digits

print(Solution().plusOne([9,9,9]))
