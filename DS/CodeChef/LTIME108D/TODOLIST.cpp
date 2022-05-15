#include <iostream>
using namespace std;

int main() {
	int tc, marks, count, inp;
	cin >> tc;
	for(int i=0; i<tc; i++) {
	    cin >> inp;
	    count = 0;
	    for(int j=0; j<inp; j++) {
    	    cin >> marks;
    	    if(marks >= 1000)
    	        count++;
	    }
	    cout << count << '\n';
	}
	return 0;
}
