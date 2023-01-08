# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def llreversal(self, head):
        curr=head
        ptr1=None
        while(curr!=None):
            temp=curr.next
            curr.next=ptr1
            ptr1=curr
            curr=temp
        head=ptr1
        return head

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev=self.llreversal(head)
        ptr=rev
        head=None
        curmx=0
        while(ptr!=None):
            if ptr.val>=curmx:
                head=ListNode(ptr.val,head)
                curmx=ptr.val
            ptr=ptr.next
        return head