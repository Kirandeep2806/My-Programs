# User function Template for python3

class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, Items, n):
        Items.sort(key=lambda x: x.value/x.weight, reverse=True)
        curW = 0
        profits = 0
        for i in Items:
            print(i.value, i.weight)
            curW += i.weight
            if curW < W:
                profits += i.value
            else:
                curW -= i.weight
                fraction = (W-curW)/i.weight
                profits += i.value*fraction
                break
        return profits

        # code here

# {
#  Driver Code Starts
# Initial Template for Python 3
# Contributed by : Nagendra Jha


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, W = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        Items = [Item(0, 0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]

        ob = Solution()
        print("%.2f" % ob.fractionalknapsack(W, Items, n))

# } Driver Code Ends
