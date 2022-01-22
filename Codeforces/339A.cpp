#include<bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string inp;
    int trackCount[3] = {0, 0, 0};
    cin >> inp;
    for(int i=0; inp[i]!='\0'; i++) {
        if(inp[i]=='1')
            trackCount[0]++;
        if(inp[i]=='2')
            trackCount[1]++;
        if(inp[i]=='3')
            trackCount[2]++;
    }

    while(trackCount[0]!=0) {
        if(trackCount[0] != 1)
            cout << "1+";
        else if(trackCount[1] || trackCount[2])
            cout << "1+";
        else
            cout << "1";
        trackCount[0]--;
    }
    while(trackCount[1]!=0) {
        if(trackCount[1] != 1)
            cout << "2+";
        else if(trackCount[2])
            cout << "2+";
        else
            cout << "2";
        trackCount[1]--;
    }
    while(trackCount[2]!=0) {
        if(trackCount[2] != 1)
            cout << "3+";
        else
            cout << "3";
        trackCount[2]--;
    }
    

}