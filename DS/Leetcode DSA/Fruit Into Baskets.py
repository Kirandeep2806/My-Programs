class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt=res=consecutives=1
        hm={fruits[0]}
        n=len(fruits)
        for i in range(1,n):
            if fruits[i] in hm:
                cnt+=1
            elif len(hm)<=1:
                hm.add(fruits[i])
                cnt+=1
            else:
                hm.remove(*(hm-{fruits[i-1]}))
                hm.add(fruits[i])
                cnt=consecutives+1
            res=max(res,cnt)
            if fruits[i]==fruits[i-1]:
                consecutives+=1
            else:
                consecutives=1
        return res
