class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        step = 1
        while(m!=n):
            m = m//2
            n = n// 2
            step *= 2
        return m*step