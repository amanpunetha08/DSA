# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def dfs(self,root,level,res):
        if not root:
            return None
        
        res[level].append(root.val)
        self.dfs(root.left,level+1,res)
        self.dfs(root.right,level+1,res)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        self.dfs(root,0,res)
        return list(res.values())
        