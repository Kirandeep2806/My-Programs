#include <iostream>
using namespace std;

int main() {
	int tc, w, x, y, z, filledTill;
	cin >> tc;
	for(int i=0; i<tc; i++) {
	    cin >> w >> x >> y >> z;
	    filledTill = y*z+w;
	    filledTill > x ? cout << "overflow" : filledTill == x ? cout << "filled" : cout << "unfilled";
	    cout << "\n";
	}
	return 0;
}
