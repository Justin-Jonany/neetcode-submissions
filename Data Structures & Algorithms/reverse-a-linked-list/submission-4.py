# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        new_head = head
        curr = head.next # save the next object
        new_head.next = None # cut it off
        while curr: # iterate on the next object
            temp = curr.next # the next item to recurse on
            curr.next = new_head # put the new object in front
            new_head = curr # it becomes the new head
            curr = temp # now we go to the supposed next item

        return new_head

        # curr = 3 -> (2 -> (1))
        # temp = 2 -> (1)
        # 2 -> 3
        # 


        