class Solution:
    def checkValidString(self, s: str) -> bool:
        from collections import deque
        stack = deque()
        star = deque()
        for i, x in enumerate(s):
            if x == '(':
                stack.append(i)
            elif x == '*':
                star.append(i)
            else:
                if not stack and not star:
                    return False
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
        
        while stack and star:
            if stack.pop() > star.pop():
                return False
        
        if not stack:
            return True
        else:
            return False