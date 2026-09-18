class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = nums[0];       // Initialize with the first element
        int current_sum = nums[0];   // Running sum

        for (int i = 1; i < nums.size(); i++) {
            // Either extend the current subarray or start fresh
            current_sum = max(nums[i], current_sum + nums[i]);
            max_sum = max(max_sum, current_sum);
        }

        return max_sum;
    }
};