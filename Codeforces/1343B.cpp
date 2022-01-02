#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, i, testcases;
    cin >> testcases;
    for (int t_case = 0; t_case < testcases; t_case++) {
        cin >> n;
        if (((n / 2) % 2) & 1)
            cout << "NO" << "\n";
        else {
            cout << "YES" << "\n";
            for (i = 2; i <= n; i += 2)
                cout << i << " ";
            for (i = 1; i < n - 1; i += 2)
                cout << i << " ";
            cout << i+n/2 << "\n";
        }
    }
    return 0;
}