# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        # def ll_to_string(n):
        #     s = ""
        #     while n:
        #         s += f"{n.val}->"
        #         n = n.next
        #     return s[:-2]
        curr = head
        # while curr:
        for i in range((len(stack) // 2) + 1):
            # end = stack.pop()
            front = stack[i]
            end = stack[-i-1]
            # print(f'front: {front.val}\tend: {end.val}. head: {ll_to_string(head)}')
            temp = curr.next
            curr.next = end
            curr.next.next = temp
            curr = curr.next.next
        curr.next = None
        


# 2 -> 4 -> 6 -> 8 -> 10
# [2, 4, 6]
# 2 -> 10 -> 4 -> 8 -> 6 -> 8 -> 10
# curr = 6 -> 8 -> 10