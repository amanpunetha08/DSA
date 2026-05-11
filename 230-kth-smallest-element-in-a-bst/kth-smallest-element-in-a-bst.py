# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def print(self,root,ans,k):
        if not root:
            return
        if len(ans) <k:
            self.print(root.left,ans,k)
            ans.append(root.val)
            self.print(root.right,ans,k)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        self.print(root,ans,k)
        return ans[k-1]
        