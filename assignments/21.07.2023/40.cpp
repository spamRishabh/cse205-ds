#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;
        sort(candidates.begin(), candidates.end()); 
        backtrack(candidates, target, 0, current, result);
        return result;
    }

private:
    void backtrack(vector<int>& candidates, int target, int start, vector<int>& current, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(current);
            return;
        }

        for (int i = start; i < candidates.size(); ++i) {
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue; 
            }

            if (candidates[i] <= target) {
                current.push_back(candidates[i]);
                backtrack(candidates, target - candidates[i], i + 1, current, result);
                current.pop_back();
            }
        }
    }
};