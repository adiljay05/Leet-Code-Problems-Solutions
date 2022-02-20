# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mm = ListNode()
        m = mm
        carry = 0
        while l1 or l2 or carry: # iterate until elements in one of the list or carry has value
            v1 = v2 = 0
            if l1: # if l1 has elements, get next value and move ptr
                v1 = l1.val
                l1 = l1.next
            if l2: # if l2 has elements, get next value and move ptr
                v2 = l2.val
                l2 = l2.next
            
            sum_ = v1+v2+carry
            carry = int(sum_/10) # get the carry by floor (integer) devision
            m.next = ListNode(sum_%10) # add the remainder value to the list
            
            m = m.next # move pointer to next (new value will be added here)
            
        return mm.next # return the start of the list (rest of the elements can be accessed from start)
            
        