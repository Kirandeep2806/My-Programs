from functools import lru_cache

matrix = [[0,10,15,20],
		  [5,0,9,10],
		  [6,13,0,12],
		  [8,8,9,0]]

def permutations(i, n, res):
	if i == n:
		summ = 0
		for k in range(n-1):
			summ += matrix[arr[k]][arr[k+1]]
		summ += matrix[arr[-1]][0]
		summ += matrix[0][arr[0]]
		res[0] = min(res[0], summ)
		return
	for j in range(i,n):
		arr[i], arr[j] = arr[j], arr[i]
		permutations(i+1, n, res)
		arr[i], arr[j] = arr[j], arr[i]


n = 4
arr = [i for i in range(1,n)]
res = [float("inf")]
permutations(0, n-1, res)
print(res[0])
