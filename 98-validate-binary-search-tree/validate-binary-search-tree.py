# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,min,max):
        if not root:
            return True
        
        if min and root.val <= min.val:
            return False
        if max and root.val >= max.val:
            return False
        
        return self.solve(root.left,min,root) and self.solve(root.right,root,max)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root,None,None)
        