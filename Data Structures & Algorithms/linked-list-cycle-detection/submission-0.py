# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # max length is 1000
        counter = 0
        while head:
            head = head.next
            counter += 1
            if counter > 1000:
                return True

        return False