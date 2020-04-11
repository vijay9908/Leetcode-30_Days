class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max , global_max = nums[0],nums[0]
        for ele in nums[1:]:
            current_max = max(ele,current_max+ele)
            global_max = max(current_max,global_max)
        return global_max