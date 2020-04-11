class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a1 , a2 = [] , []
        for ele in S:
            if ele != '#':
                a1.append(ele)
            else:
                if len(a1)>0:
                    a1.pop()
        
        for ele in T:
            if ele != '#':
                a2.append(ele)
            else:
                if len(a2)>0:
                    a2.pop()
        
        return a1==a2
                
        