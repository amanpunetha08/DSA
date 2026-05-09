# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if not root:
            return True,0
        left,left_height = self.check(root.left)
        if not left:
            return False,0
        right,right_height = self.check(root.right)
        if not right:
            return False,0
        
        if abs(left_height - right_height) >1:
            return False,0
        return True,1 + max(left_height,right_height)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        resutl,_  = self.check(root)
        return resutl       
        