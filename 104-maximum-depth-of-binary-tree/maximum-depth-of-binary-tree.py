# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMaxlevel(self,root):
        if not root:
            return 0
        left = self.findMaxlevel(root.left)
        right = self.findMaxlevel(root.right)
        return max(left,right) +1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxlevel = self.findMaxlevel(root)
        return maxlevel
        