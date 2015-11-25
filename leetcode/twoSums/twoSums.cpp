class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int>maps;
        for(int i=0; i<nums.size();i++){
            if(maps.find(target-nums[i])!=maps.end()){
                vector<int>v = {maps[target-nums[i]],i+1};
                return v;
            }
        
        maps[nums[i]]=i+1;
    }
    }
};
