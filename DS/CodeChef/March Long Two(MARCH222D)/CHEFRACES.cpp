#include "bits/stdc++.h" 
using namespace std; 
#define max(a, b) (a < b ? b : a) 
#define min(a, b) ((a > b) ? b : a) 
#define fr(i, a, b) for (ll i = a; i < b; i++)
#define rf(i, a, b) for (ll i = a; i >= b; i--)
#define inf 1000000000000000003 
const int mod = 1'000'000'007;
#define ll long long
#define ini(a, i) memset(a, i, sizeof(a))
#define vi vector<int>
#define mp map<ll,ll>
#define ii pair<int, int>
#define vii vector<ii>
#define sz(s) s.size()
#define fi first
#define se second 
#define endl '\n'
#define prec(n) fixed<<setprecision(n)
#define maxpq priority_queue<int>
#define minpq priority_queue<int, vector<int>, greater<int> >
#define pb push_back
#define pob pop_back
#define all(x) (x).begin(),(x).end()
/*---------------------------------------------------------------------------------------------------------------------------*/
ll expo(ll a, ll b, ll mod) {ll res = 1; while (b > 0) {if (b & 1)res = (res * a) % mod; a = (a * a) % mod; b = b >> 1;} return res;}
void extendgcd(ll a, ll b, ll*v) {if (b == 0) {v[0] = 1; v[1] = 0; v[2] = a; return ;} extendgcd(b, a % b, v); ll x = v[1]; v[1] = v[0] - v[1] * (a / b); v[0] = x; return;} //pass an arry of size1 3
ll mminv(ll a, ll b) {ll arr[3]; extendgcd(a, b, arr); return arr[0];} //for non prime b
ll mminvprime(ll a, ll b) {return expo(a, b - 2, b);}
bool revsort(ll a, ll b) {return a > b;}
void swap(int &x, int &y) {int temp = x; x = y; y = temp;}
ll combination(ll n, ll r, ll m, ll *fact, ll *ifact) {ll val1 = fact[n]; ll val2 = ifact[n - r]; ll val3 = ifact[r]; return (((val1 * val2) % m) * val3) % m;}
void google(int t) {cout << "Case #" << t << ": ";}
vector<ll> sieve(int n) {int*arr = new int[n + 1](); vector<ll> vect; for (int i = 2; i <= n; i++)if (arr[i] == 0) {vect.push_back(i); for (int j = 2 * i; j <= n; j += i)arr[j] = 1;} return vect;}
ll mod_add(ll a, ll b, ll m) {a = a % m; b = b % m; return (((a + b) % m) + m) % m;}
ll mod_mul(ll a, ll b, ll m) {a = a % m; b = b % m; return (((a * b) % m) + m) % m;}
ll mod_sub(ll a, ll b, ll m) {a = a % m; b = b % m; return (((a - b) % m) + m) % m;}
ll mod_div(ll a, ll b, ll m) {a = a % m; b = b % m; return (mod_mul(a, mminvprime(b, m), m) + m) % m;}  //only for prime m
ll phin(ll n) {ll number = n; if (n % 2 == 0) {number /= 2; while (n % 2 == 0) n /= 2;} for (ll i = 3; i <= sqrt(n); i += 2) {if (n % i == 0) {while (n % i == 0)n /= i; number = (number / i * (i - 1));}} if (n > 1)number = (number / n * (n - 1)) ; return number;} //O(sqrt(N))
int binarySearch(int arr[], int left, int right, int x) {while (left <= right) {int mid = left + (right - left) / 2;if (arr[mid] == x) {return mid;} else if (arr[mid] < x) {left = mid + 1;} else {right = mid - 1;}}return -1;}
bool sign(int num){return num > 0;}
bool isPrime(long long n){int skip=0;if(n<2)return false;else if(n==2)return true;long long limit=sqrt(n);if(n%2==0)return false;for(int j=3; j<=limit; j+=2){if(n%j==0)return false;}return true;}
/*---------------------------------------------------*/
int main() 
{ 
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    cout<<fixed,cout<<setprecision(10);
    int a,b,x,y,i,medalCount,t;
    cin >> t;
    fr(i,0,t){
        medalCount=0;
        cin>>a>>b>>x>>y;
        if(a!=x && a!=y)
            medalCount++;
        if(b!=x && b!=y)
            medalCount++;
        cout << medalCount << "\n";
    }

}
/*---------------------------------------------------*/