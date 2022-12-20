#!/usr/bin/python3

from typing import List

class Solution:
	def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
		visited=set()
		q=[]
		for i in rooms[0]:
			q.append(i)
			visited.add(i)
		visited.add(0)
		while q:
			i=q.pop(0)
			for v in rooms[i]:
				if v not in visited:
					q.append(v)
					visited.add(v)
		if visited.__len__()==rooms.__len__():
			return True
		return False

rooms = [[1,3],[3,0,1],[2],[0]]
print(Solution().canVisitAllRooms(rooms))
