#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--) {
		int x,y,k;
		cin>>x>>y>>k;
		int diff=abs(x-y);
		cout<<ceil((float)diff/(float)k)<<"\n";
	}
	return 0;
}
