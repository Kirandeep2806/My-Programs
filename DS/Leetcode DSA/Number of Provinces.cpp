#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    void dfs(int i, int n, vector<vector<int>> &isConnected, vector<int> &v) {
        v[i]=1;
        for(int j=0;j<n;j++){
            if(isConnected[i][j] && !v[j])
                dfs(j, n, isConnected, v);
        }
    }

    int findCircleNum(vector<vector<int>> &isConnected) {
        int n=isConnected.size(),res=0;
        vector<int> v(n,0);
        for(int i=0;i<n;i++) {
            if(!v[i]){
                dfs(i, n, isConnected, v);
                res++;
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<vector<int>> graph;
    int n,val;
    cin>>n;
    for(int i=0;i<n;i++){
        vector<int> oneD;
        for(int j=0;j<n;j++){
            cin>>val;
            oneD.push_back(val);
        }
        graph.push_back(oneD);
    }
    cout<<s.findCircleNum(graph);
}
