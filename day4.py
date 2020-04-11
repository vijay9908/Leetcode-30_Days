class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        def swap(list,i,j):
            list[i] , list[j] = list[j] , list[i]
        
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                swap(nums,j,i)
                j += 1
            
            
            
        