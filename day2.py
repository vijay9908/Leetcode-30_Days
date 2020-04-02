class Solution:
    def isHappy(self, n: int) -> bool:
        def sosquares(num):
            return sum(int(c)**2 for c in str(n))
        se = 1
        count =0
        while(n>0 and count<99):
            n = sosquares(n)
            if n==1:
                se = 0
                break
            else:
                count +=1

        return True if se==0 else False


        