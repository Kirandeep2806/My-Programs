#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, num;
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> num;
        int sq = sqrt(num), indicator=0;
        for(int j=2; j<=sq; j++) {
            if(num%j == 0) {
                indicator++;
                break;
            }
        }
        if(!indicator && num!=1)
            cout << "Prime\n";
        else
            cout << "Not prime\n";
    }
    return 0;
}
