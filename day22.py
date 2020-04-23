class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        prev_sum = defaultdict(int)
        res , curr = 0 , 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr == k:
                res += 1
            if curr-k in prev_sum:
                res += prev_sum[curr-k]
            prev_sum[curr] += 1
        return res
                
                