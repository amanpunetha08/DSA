# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,result,ans,targetSum):
        if not root:
            return
        
        targetSum -=root.val
        ans.append(root.val)
        if not root.left and not root.right and targetSum ==0:
            result.append(ans[:])
        
        self.check(root.left,result,ans,targetSum)
        self.check(root.right,result,ans,targetSum)
        ans.pop()
        return
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        ans = []
        self.check(root,result,ans,targetSum)
        return result
        