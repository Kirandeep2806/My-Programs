# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # l1 should be always small
        if l1.val > l2.val:
            l1,l2 = l2,l1
        res = l1
        while l1!=None and l2!=None:
            temp = None
            while l1!=None and l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            temp.next = l2
            l1,l2 = l2,l1
        return res
