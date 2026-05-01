# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head,k):
        new_head,temp = None,head
        while k:
            new_node = temp.next
            temp.next = new_head
            new_head =temp
            temp = new_node
            k-=1
        return new_head
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        ptr = head

        while count<k and ptr:
            ptr = ptr.next
            count+=1

        if count ==k:
            reverse_node = self.reverse(head,k)
            head.next = self.reverseKGroup(ptr,k)
            return reverse_node
        return head
        


        