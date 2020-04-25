class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = 0
        for i in range(len(nums)):
            if i > jumps:
                return False
            else:
                k = i+nums[i]
                jumps = max(jumps,k)
                if jumps >= len(nums)-1:
                    return True
            
            
            
            
            
            
            
            