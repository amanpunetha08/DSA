# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,maxSum):
        if not root:
            return 0
        
        left_sum = max(self.helper(root.left,maxSum),0)
        right_sum = max(self.helper(root.right,maxSum),0)
        maxSum[0] = max(maxSum[0],root.val + left_sum + right_sum)
        return root.val + max(left_sum,right_sum)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [float('-inf')]
        self.helper(root,maxSum)   
        return maxSum[0]     