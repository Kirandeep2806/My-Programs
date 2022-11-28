class Solution {
    public:
        vector<vector<int>> findWinners(vector<vector<int>>& matches) {
            vector<vector<int>> res;
            map<int,int> players;
            set<int> all_players;
            for(vector<int> &i:matches) {
                players[i[1]]++;
                all_players.insert(i[0]);
                all_players.insert(i[1]);
            }
            vector<int> aux_res;
            for(const int &i:all_players)
                if(players.find(i)==players.end())
                    aux_res.push_back(i);
            res.push_back(aux_res);
            aux_res.clear();
            for(pair<const int,int> &i:players)
                if(i.second==1)
                    aux_res.push_back(i.first);
            res.push_back(aux_res);
            return res;
        }
};



