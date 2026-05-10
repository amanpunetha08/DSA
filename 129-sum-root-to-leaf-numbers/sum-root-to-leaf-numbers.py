# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,total,currentSum):
        if not root:
            return 0
        
        currentSum = currentSum* 10 + root.val
        if not root.left and not root.right:
            total[0] += currentSum
        
        return self.helper(root.left,total,currentSum) + self.helper(root.right,total,currentSum)
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = [0]
        self.helper(root,total,0)
        return total[0]
        

        