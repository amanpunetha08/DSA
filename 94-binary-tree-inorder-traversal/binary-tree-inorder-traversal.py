# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printInorderTraversal(self,root: Optional[TreeNode],ans: List):
        if not root:
            return
        
        self.printInorderTraversal(root.left,ans)
        ans.append(root.val)
        self.printInorderTraversal(root.right,ans)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.printInorderTraversal(root,ans)
        return ans
        