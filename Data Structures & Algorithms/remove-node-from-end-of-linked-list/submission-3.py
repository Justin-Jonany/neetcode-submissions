# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        normal = head
        headstart = head
        for _ in range(n):
            headstart = headstart.next
        if headstart is None:
            return head.next

        while headstart.next:
            normal = normal.next
            headstart = headstart.next
        normal.next = normal.next.next
        return head

        # [2, 3, 4] n = 3
        # normal 0
        # headstart None
        # 

        # [1] n = 1
        # headstart = None
        

        
        # two pass v2
        # length = 0
        # curr = head
        # while curr:
        #     curr = curr.next
        #     length += 1
        

        # index = length - n
        # dummy = ListNode(0, head)
        # curr = dummy
        # for i in range(index):
        #     curr = curr.next
        # curr.next = curr.next.next
        # head = dummy.next
        # return head

        # two pass v2
        # length = 0
        # curr = head
        # while curr:
        #     curr = curr.next
        #     length += 1
        

        # index = length - n
        # if index == 0:
        #     head = head.next
        #     return head

        # curr = head
        # for i in range(index - 1):
        #     curr = curr.next
        # curr.next = curr.next.next
        # return head


# [1,2,3,4, 5,6] index = 3
# n = 3
# 0 1 2 3
# 3 4 5 6
