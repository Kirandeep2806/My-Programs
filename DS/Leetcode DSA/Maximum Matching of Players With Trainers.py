#!/usr/bin/python3

from typing import List

class Solution:
	def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
		players.sort()
		trainers.sort()
		n=len(players)
		m=len(trainers)
		print(n,m)
		i=0
		j=0
		res=0
		while i<n and j<m:
			if players[i]<=trainers[j]:
				i+=1
				j+=1
				res+=1
				continue
			j+=1
		return res

players=eval(input())
trainers=eval(input())
res = Solution().matchPlayersAndTrainers(players, trainers)
print(res)
