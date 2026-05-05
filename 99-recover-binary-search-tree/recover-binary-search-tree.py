# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,prev,first,second):
        if not root:
            return
        
        self.inorder(root.left,prev,first,second)
        if prev[0] and prev[0].val > root.val:
            if first[0] is None:
                first[0] = prev[0]
            second[0] = root
        prev[0] = root
        self.inorder(root.right,prev,first,second)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = [None]
        second = [None]
        prev = [None]
        self.inorder(root,prev,first,second)
        first[0].val,second[0].val = second[0].val, first[0].val
        