#!/usr/bin/python3
#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        l = {}
        res = {}
        for string in words:
            temp = {}
            for letter in string:
                if temp.get(letter, 0) == 0:
                    temp[letter] = 0
                temp[letter] += 1
            for i in l:
                if l[i] == temp:
                    res[i].append(string)
                    break
            else:
                l[string] = temp
                res[string] = [string]
        returnRes = []
        for i in res:
            returnRes.append(res[i])
        return returnRes


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends