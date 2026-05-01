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
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            # count k nodes
            count = 0
            ptr = prev.next
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            if count < k:
                break

            # reverse k nodes
            cur = prev.next
            reverse_node = self.reverse(cur, k)

            prev.next = reverse_node
            cur.next = ptr
            prev = cur

        return dummy.next
        


        