#include<bits/stdc++.h>
using namespace std;
const int mod = 1000000007;
#define ll long long

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    cout << fixed, cout << setprecision(10);
    ll t,x,y;
    cin >> t;
    int lcmVal, consider;
    // cout << 99999999999999999%mod << endl;
    while(t--) {
        cin >> x >> y;
        if(x == y)
            cout << x;
        else {
            lcmVal = lcm(x,y);
            if(x == lcmVal)
                consider = lcmVal/y;
            else if(y == lcmVal)
                consider = lcmVal/x;
            else
                consider = lcmVal/x + lcmVal/y;
            cout << consider+lcmVal;
        }
    }

}
