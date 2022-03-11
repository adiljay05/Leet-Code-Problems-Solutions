# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        res, ll_len = head, 0
        # Loop to find length of Linked List
        while head:
            ll_len += 1
            head = head.next
            
        head = res
        k %= ll_len # Remove redundant rotations
        while k:
            # Simulate Linked List rotations
            while head:
                if head.next.next == None:
                    head.next.next = res
                    res = head.next
                    head.next = None
                head = head.next
            head = res
            k -= 1
            
        return res