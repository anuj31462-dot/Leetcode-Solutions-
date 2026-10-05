class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int>num;
        for ( int i = 0 ; i  < nums.size(); i++){
            if ( nums[i]!= 0){

                num.push_back(nums[i]);
            }
            
        }
        while (num.size() < nums.size()){
            num.push_back(0);
        }
        for(int i = 0 ; i < nums.size() ; i++){
            nums[i] = num[i];
        }
        
    }
};