class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def convert(s): 
            new = "" 
            for x in s: 
                new += x
            return new 
        
        s = list(s.strip())
        
        def shifts(s,shift):
            k = 0
            for i in range(len(shift)):
                if shift[i][0]==1:
                    k += shift[i][1]
                else:
                    k -= shift[i][1]
            return k
        w = shifts(s,shift)
        q = []
        for i in range(len(s)):
            q.append(s[i-w%len(s)])
        return convert(q)
                    
            
            