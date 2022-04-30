#include<bits/stdc++.h>

using namespace std; 

int main() 
{ 
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    cout<<fixed,cout<<setprecision(10);
    int n,a,b,c,d;
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> a >> b >> c >> d;
        if(pow(a,2)/pow(b,2) == pow(c, 3)/ pow(d, 3))
            cout << "Yes" << "\n";
        else
            cout << "No" << "\n";
    }
}