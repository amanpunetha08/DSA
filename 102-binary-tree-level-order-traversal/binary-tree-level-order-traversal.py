# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def printLevelOrder(self,root,mapper,level):
        if not root:
            return
        mapper[level].append(root.val)
        self.printLevelOrder(root.left,mapper,level+1)
        self.printLevelOrder(root.right,mapper,level+1)
        return

        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapper = defaultdict(list)
        self.printLevelOrder(root,mapper,0)
        return list(mapper.values())
        