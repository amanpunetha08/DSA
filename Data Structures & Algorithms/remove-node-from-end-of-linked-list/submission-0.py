# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listlen = 0
        temp = head
        while temp:
            temp = temp.next
            listlen+=1
        
        removenode = listlen - n
        if removenode == 0:
            return head.next
        
        temp = head
        for i in range(listlen - 1):
            if i + 1  == removenode:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head

            

        

        