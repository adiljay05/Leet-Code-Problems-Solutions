# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for i in range(0,n):
            if fast:
                fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            # print(slow.val)
            # print(fast.val)
            # print()
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
