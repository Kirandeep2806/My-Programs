from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        r=[0,0,1,-1]
        c=[1,-1,0,0]
        axes=(sr,sc)
        q=deque((axes,))
        visited=[[0]*n for i in range(m)]
        col=image[sr][sc]
        while q:
            t=q.popleft()
            if not visited[t[0]][t[1]]:
                image[t[0]][t[1]]=color
                visited[t[0]][t[1]]=1
                # print(t,image,col)
                for i in range(4):
                    r1=t[0]+r[i]
                    c1=t[1]+c[i]
                    # print(r1, c1)
                    
                    if 0<=r1<m and 0<=c1<n and image[r1][c1]==col:
                        q.append((r1,c1))
        return image
