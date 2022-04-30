#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int t,sum,res,iter,r_0,r_1,r_2,g_0,g_1,g_2,b_0,b_1,b_2,min_1;
	cin >> t;
	while(t--) {
	    cin >> sum;
	    res=0;
	    cin >> r_0 >> g_0 >> b_0 >> r_1 >> g_1 >> b_1 >> r_2 >> g_2 >> b_2;
	    res += min(g_0, r_1)+min(b_0, r_2)+min(b_1,g_2);
	    min_1 = abs(g_0-r_1);
	    if(min_1)
	        res += 2*min_1;
        cout << res << "\n";
	}
	return 0;
}
