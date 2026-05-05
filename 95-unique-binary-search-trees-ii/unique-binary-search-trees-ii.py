# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generate(self,start,end):
        if start > end:
            return [None]
        
        all_trees = []
        for root_val in range(start,end+1):
            left_trees = self.generate(start,root_val-1)
            right_trees = self.generate(root_val+1,end)
            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(root_val)
                    root.left = l
                    root.right = r
                    all_trees.append(root)
        return all_trees

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate(1,n)

        