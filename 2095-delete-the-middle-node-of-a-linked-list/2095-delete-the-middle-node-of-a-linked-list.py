# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            head=head.next
            return head
        cur = head
        prev = None
        double_cur = head
        while double_cur and double_cur.next:
            prev = cur
            cur = cur.next
            double_cur = double_cur.next.next
        
        prev.next = cur.next
        return head