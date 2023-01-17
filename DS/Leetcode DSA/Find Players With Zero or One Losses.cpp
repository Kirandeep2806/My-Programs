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


// Efficient Approach

static vector<vector<int>> findWinners(const vector<vector<int>>& matches) noexcept {
    array<bool, 100001> played = {};
    array<int, 100001> losses = {};
    
    for (const vector<int>& match : matches) {
        played[match[0]] = true;
        played[match[1]] = true;
        ++losses[match[1]];
    }
    
    vector<vector<int>> ans(2);

    for (int i = 0; i < size(played); ++i) {
        if (played[i]) {
            if (losses[i] == 0) {
                ans[0].push_back(i);
            } else if (losses[i] == 1) {
                ans[1].push_back(i);
            }
        }
    }

    return ans;
}
