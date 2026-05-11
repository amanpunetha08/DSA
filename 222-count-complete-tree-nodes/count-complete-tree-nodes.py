# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_h = 0
        node = root
        while node:
            left_h +=1
            node = node.left
        
        right_h =0
        node = root
        while node:
            right_h+=1
            node = node.right
        
        if left_h == right_h:
            return 2**left_h -1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)        