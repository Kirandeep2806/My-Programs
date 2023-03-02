class Solution:
    def compress(self, chars: List[str]) -> int:
        ptr=0
        cnt=1
        i=1
        n=chars.__len__()
        while i<n:
            if chars[i]==chars[i-1]:
                cnt+=1
            else:
                chars[ptr]=chars[i-1]
                if cnt>1:
                    for digit in str(cnt):
                        ptr+=1
                        chars[ptr]=str(digit)
                ptr+=1
                cnt=1
            i+=1
        chars[ptr]=chars[i-1]
        if cnt>1:
            for digit in str(cnt):
                ptr+=1
                chars[ptr]=str(digit)
        return ptr+1