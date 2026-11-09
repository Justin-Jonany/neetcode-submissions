# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        new = ListNode(curr.val)

        while curr.next:
            new = ListNode(curr.next.val, new)
            curr = curr.next
        
        return new
        