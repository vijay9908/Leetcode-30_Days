class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            k = k^nums[i]
        return k