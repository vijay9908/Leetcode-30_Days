# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left),height(node.right))
        
        def diameter(root):
            if root is None:
                return 0
            
            l_height = height(root.left)
            r_height = height(root.right)
            
            l_dia = diameter(root.left)
            r_dia = diameter(root.right)
            
            return max(l_height+r_height,max(l_dia,r_dia))
        
        return diameter(root)
            
            
            