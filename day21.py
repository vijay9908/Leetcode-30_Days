# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        a = binaryMatrix.dimensions()
        count = 0 
        beal=False
        n , m = a[0] , a[1]
        if n==0 or m==0:
            return -1
        result , r,c = -1,0,m-1
        while r<n and c>=0:
            if binaryMatrix.get(r,c)==1:
                result = c
                c -= 1
            else:
                r += 1
        return result
                
            