# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        double_cur = head
        while double_cur and double_cur.next :
            cur = cur.next
            double_cur = double_cur.next.next
        
        return cur