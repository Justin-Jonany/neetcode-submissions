# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
# 1. iterate through head and get length of n
# 2. second pass and rmeove the nth ndoe from the list  
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        

        index = length - n
        if index == 0:
            head = head.next
            return head

        curr = head
        for i in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head


# [1,2,3,4]
# length = 4
# index = 2
# 1 2 3