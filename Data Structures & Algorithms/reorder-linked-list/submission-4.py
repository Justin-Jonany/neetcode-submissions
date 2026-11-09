# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        i, j = 0, len(stack) - 1
        while i < j:
            stack[i].next = stack[j]
            stack[j].next = stack[i+1]
            i += 1
            j -= 1
        stack[i].next = None
        
        


# 2 -> 4 -> 6
# [2 -> 6 -> 4 -> 6, 4->6, 6 -> 4->6]


