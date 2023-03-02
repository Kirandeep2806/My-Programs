#include <bits/stdc++.h>
using namespace std;

int dfs(int i, vector<int> &heights, vector<int> &dp) {
    if(i==0) return 0;
    if(dp[i]!=-1) return dp[i];

    int left = dfs(i-1, heights, dp) + abs(heights[i]-heights[i-1]);
    int right=INT_MAX;
    if(i>1)
        right = dfs(i-2, heights, dp) + abs(heights[i]-heights[i-2]);
    return dp[i]=min(left, right);
}

int frogJump(int n, vector<int> &heights) {
    vector<int> dp(n,-1);
    return dfs(n-1,heights,dp);
}

int main() {
    int t,n,val;
    cin>>t;
    while(t--) {
        cin>>n;
        vector<int> arr;
        for(int i=0;i<n;i++) {
            cin>>val;
            arr.push_back(val);
        }
        cout<<frogJump(n,arr)<<endl;
    }
}
