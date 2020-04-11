class Solution:
    def countElements(self, arr: List[int]) -> int:
        k = 0
        for ele in arr:
            if ele+1 in arr:
                k +=1
        return k