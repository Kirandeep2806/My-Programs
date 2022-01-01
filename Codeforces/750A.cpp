#include<bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int qns, travelTime, i;
    cin >> qns >> travelTime;
    for(i=0; (240 - (travelTime +(5*(i*(i+1))/2))) >= 0 && i!=qns+1; i++ );
    i -= 1;
    cout << i;

    return 0;
}