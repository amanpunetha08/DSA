# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeBuild(self,preorder,search_map,pre_index,left,right):
        if left > right:
            return None, pre_index
        
        root = TreeNode(preorder[pre_index])
        mid = search_map[root.val]

        root.left,pre_index = self.treeBuild(preorder,search_map,pre_index+1,left,mid - 1)
        root.right,pre_index = self.treeBuild(preorder,search_map,pre_index,mid + 1,right)

        return root,pre_index
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        search_map =  dict()
        for i in range(len(inorder)):
            search_map[inorder[i]] = i
        
        root, _ = self.treeBuild(preorder,search_map,0,0,len(inorder)-1)
        return root

        
        

            

        