# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if not root:
            return 0
        
        left = self.check(root.left)
        right = self.check(root.right)
        if not root.left:
            return 1 + right
        if not root.right:
            return 1 + left
        return 1+ min(left,right)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.check(root)
        