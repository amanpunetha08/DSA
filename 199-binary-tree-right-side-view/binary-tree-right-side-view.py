# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        while queue:
            ans = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if not ans:
                    ans = node
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
            result.append(ans.val)
        return result

        