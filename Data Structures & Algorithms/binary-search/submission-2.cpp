class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int idx = (right + left) / 2;

            if (nums[idx] < target)
                left = idx + 1;
            else if (nums[idx] > target)
                right = idx - 1;
            else
                return idx;
        }

        return -1;
    }
};
