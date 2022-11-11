#!/usr/bin/python3

class Solution:
	def __init__(self):
		self.temp = 0
	def myPow(self, x: float, n: int) -> float:
		if n==0:
			return 1
		res = self.myPow(x, int(n/2))
		res = res*res
		if n%2==0:
			return res
		self.temp += 1
		if self.temp==1:
			if n<0:
				return 1/(res*x)
		elif self.temp>1:
			if n<0:
				return res*(1/x)
		return res*x

print(Solution().myPow(int(input()), int(input())))
