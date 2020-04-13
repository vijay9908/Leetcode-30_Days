class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while True:
            if len(stones)==1:
                return stones[0]
            elif len(stones)==0:
                return 0
            else:
                q1 , q2 = stones[0] , stones[1]
                stones = stones[2:]
                if q1 != q2:
                    stones.append(abs(q1-q2))
                    stones.sort(reverse=True)
        