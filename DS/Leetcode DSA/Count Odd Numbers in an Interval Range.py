class Solution:
    def countOdds(self, l: int, h: int) -> int:
        if l%2:l-=1
        if h%2:h+=1
        return (h-l)//2