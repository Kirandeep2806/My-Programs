class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();
        int m1[n],m2[n],j=1,water_trapped=0;
        m1[0]=*height.begin();
        for(auto i=height.begin()+1;i!=height.end();i++, j++)
            m1[j]=max(m1[j-1],*i);
        j--;
        m2[j]=*height.rbegin();
        j--;
        for(auto i=height.rbegin()+1;i!=height.rend();i++, j--)
            m2[j]=max(m2[j+1],*i);
        for(int i=0;i<n;i++)
            water_trapped+=min(m1[i],m2[i])-(*(height.begin()+i));
        return water_trapped;
    }
};
