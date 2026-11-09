# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head.val if head else "None")
        # if head is None or head.next is None:
        #     return head
        # new_head = self.reverseList(head.next)
        # new_head.next = head

        def print_ll(n):
            s = ""
            while n:
                s += f"{n.val}->"
                n = n.next
            print(s[:-2])
        # print_ll(head)
        if head is None:
            return head
        new_head = head
        curr = head.next # save the next object
        new_head.next = None # cut it off
        while curr: # recurse on the next object
        # for i in range(3):
            print_ll(curr)
            # print(head.val)
            temp = curr.next # the next item to recurse on
            curr.next = new_head # put curr in front
            new_head = curr # it becomes the new head
            curr = temp 

        return new_head

        # curr = 3 -> (2 -> (1))
        # temp = 2 -> (1)
        # 2 -> 3
        # 


        