#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    ll n, inp;
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> inp;
        if(inp == 1 || !inp)
            cout << "No" << "\n";
        else
            cout << "Yes" << "\n";
    }
}