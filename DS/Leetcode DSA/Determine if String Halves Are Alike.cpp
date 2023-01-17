class Solution {
    public:
        bool halvesAreAlike(string str) {
            int c1=0,c2=0;
            unordered_set<char> s({'a','e','i','o','u'});
            for(int i=0,j=str.length()/2;i<str.length()/2;i++,j++) {
                if(s.find(tolower(str[i]))!=s.end())
                    c1++;
                if(s.find(tolower(str[j]))!=s.end())
                    c2++;
            }
            if(c1!=c2)
                return false;
            return true;
        }
};
