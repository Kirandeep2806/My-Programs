from typing import List

class Solution:
	def comparision(self, n, s1, s2):
		cnt=0
		for i in range(n):
			if s1[i]!=s2[i]:
				cnt+=1
		if cnt<=2:
			return True
		return False


	def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
		res=[]
		n=queries.__len__()
		m=dictionary.__len__()
		str_length=queries[0].__len__()
		i=j=0
		s=set()
		for i in queries:
			for j in dictionary:
				if self.comparision(str_length, i, j):
					break
			else:
				continue
			res.append(i)
		return res


queries = eval(input())
dictionary = eval(input())
s = Solution().twoEditWords(queries, dictionary)
print(s)
