#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int n;
    cin >> n;
    for(int i=0; i<n; i++) {
        ll a, b, counterStart, res=1;
        cin >> a >> b;
        res <<= min(b, (ll)10);
        if(res > a)
            cout << a << "\n";
        else {
            counterStart = b-10<=0 ? 0 : b-10;
            for(int j=0; j<counterStart; j++) {
                res *= 3;
                if(res > a) {
                    res = a;
                    break;
                }
            }
            cout << res << "\n";
        }
    }
    return 0;
}