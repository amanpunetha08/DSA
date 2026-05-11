# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def print(self,root,ans):
        if not root:
            return
        
        self.print(root.left,ans)
        ans.append(root.val)
        self.print(root.right,ans)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        self.print(root,ans)
        return ans[k-1]
        