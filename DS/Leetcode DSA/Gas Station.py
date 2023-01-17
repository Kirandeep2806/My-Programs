#!/usr/bin/python3

from typing import List

class Solution:
	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		if sum(cost)>sum(gas):
			return -1
		sub=[gas[i]-cost[i] for i in range(len(gas))]
		res=0
		index=0
		for i in range(len(gas)):
			if gas[i]-cost[i]>res:
				res=gas[i]-cost[i]
				index=i
		return index



gas = eval(input())
cost = eval(input())
res = Solution().canCompleteCircuit(gas, cost)
print(res)
