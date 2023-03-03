#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
	void dfs(int i, int j, int n, int m, vector<vector<char>> &grid) {
		grid[i][j]='0';
		if(i-1>=0 && grid[i-1][j]=='1') dfs(i-1,j,n,m,grid);
		if(i+1<n && grid[i+1][j]=='1') dfs(i+1,j,n,m,grid);
		if(j-1>=0 && grid[i][j-1]=='1') dfs(i,j-1,n,m,grid);
		if(j+1<m && grid[i][j+1]=='1') dfs(i,j+1,n,m,grid);
	}

    int numIslands(vector<vector<char>>& grid) {
        ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
        int n=grid.size(),m=grid[0].size(),res=0;
        for(int i=0;i<n;i++){
        	for(int j=0;j<m;j++){
        		if(grid[i][j]=='1') {
        			dfs(i,j,n,m,grid);
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
