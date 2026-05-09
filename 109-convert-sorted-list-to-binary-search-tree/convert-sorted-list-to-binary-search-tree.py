# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,left,right):
        if left > right:
            return None
        mid = (left + right) //2
        left = self.helper(left,mid-1)
        root = TreeNode(self.head.val)
        self.head = self.head.next
        right = self.helper(mid+1,right)
        root.left = left
        root.right = right
        return root
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        temp = head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        self.head = head
        return  self.helper(0,count-1)
        
        