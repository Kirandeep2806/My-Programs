class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxval=''
        minval=''
        f1=-1
        for i in str(num):
            if i==f1:
                maxval+='9'
            elif f1==-1 and i!='9':
                f1=i
                maxval+='9'
            else:
                maxval+=i

        minval=str(num).replace(str(num)[0], '0')
        return int(maxval)-int(minval)


s=Solution().minMaxDifference(int(input()))
print(s)