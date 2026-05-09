# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,postorder,search_map,index,left,right):
        if left > right:
            return None, index
        
        root = TreeNode(postorder[index])
        mid = search_map[root.val]

        root.right,index = self.helper(postorder,search_map,index - 1,mid +1,right)
        root.left, index = self.helper(postorder,search_map,index,left,mid-1)

        return root,index
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        search_map = dict()
        for i in range(len(inorder)):
            search_map[inorder[i]] = i
        
        root, _ = self.helper(postorder,search_map,len(postorder)-1,0,len(inorder)-1)
        return root
        