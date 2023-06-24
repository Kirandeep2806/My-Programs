from collections import deque
class Solution:
    def minTime(self, root,target):
        q = deque([(root, None)])
        hm = {}
        while q:
            for i in range(len(q)):
                node,parent = q.popleft()
                if node.data == target:
                    target = node
                hm[node] = parent
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
        vis = set()
        time = 0
        q.append(target)
        while q:
            time += 1
            for i in range(len(q)):
                target = q.popleft()
                if (target in hm) and (hm[target]!=None) and (hm[target] not in vis):
                    vis.add(hm[target])
                    q.append(hm[target])
                if (target.left) and (target.left not in vis):
                    vis.add(target.left)
                    q.append(target.left)
                if (target.right) and (target.right not in vis):
                    vis.add(target.right)
                    q.append(target.right)
        return time-1
