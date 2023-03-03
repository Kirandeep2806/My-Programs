#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
	void dfs(int i, int j, int n, int m, vector<vector<char>> &grid, vector<vector<int>> &visited) {
		int row[4]={0,0,1,-1};
		int col[4]={1,-1,0,0};
		int px,py;
		for(int k=0;k<4;k++) {
			visited[i][j]=1;
			px=i+row[k];
			py=j+col[k];
			if((px>=0 && px<n) && (py>=0 && py<m) && grid[px][py]=='1' && !visited[px][py])
				dfs(px,py,n,m,grid,visited);
		}
	}

    int numIslands(vector<vector<char>>& grid) {
        ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
        int n=grid.size(),m=grid[0].size(),res=0;
        vector<vector<int>> visited(n,vector<int>(m,0));

        for(int i=0;i<n;i++){
        	for(int j=0;j<m;j++){
        		if(grid[i][j]=='1' && !visited[i][j]) {
        			dfs(i,j,n,m,grid,visited);
        			res++;
        		}
        	}
        }
        return res;
    }
};

int main(){
    Solution s;
    vector<vector<char>> graph;
    int n,m;
    char val;
    cin>>n>>m;
    for(int i=0;i<n;i++){
        vector<char> oneD;
        for(int j=0;j<m;j++){
            cin>>val;
            oneD.push_back(val);
        }
        graph.push_back(oneD);
    }
    cout<<s.numIslands(graph);
	return 0;
}
