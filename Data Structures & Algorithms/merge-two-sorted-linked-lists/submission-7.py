# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def _print_ll(n):
            s = ""
            while n:
                s += f"{n.val}->"
                n = n.next
            return s[:-2]
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        curr1 = list1
        curr2 = list2
        if list1.val < list2.val:
            new = list1 
            curr1 = curr1.next
        else:
            new = list2
            curr2 = curr2.next
        new_curr = new
        while curr1 and curr2:
            # print(f'new_curr: {_print_ll(new_curr)}')
            if curr1.val <= curr2.val:
                temp = curr1.next
                new_curr.next = curr1
                curr1 = temp
            else:
                temp = curr2.next
                new_curr.next = curr2
                curr2 = temp
            new_curr = new_curr.next if new_curr.next else new_curr
        # print(f'new_curr: {_print_ll(new_curr)}')
        # print(f'curr2: {_print_ll(curr2)}')
        # print(f'curr1: {_print_ll(curr1)}')
        if curr2:
            new_curr.next = curr2
        else:
            new_curr.next =curr1
        return new

# 1 -> 1 -> 3 -> 5
# temp 2 -> 4
# 1 -> 3 -> 5



# class Solution:
#     def mergeHelper(slef, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         # list1 is smaller
#         # def _print_ll(n):
#         #     s = ""
#         #     while n:
#         #         s += f"{n.val}->"
#         #         n = n.next
#         #     return s[:-2]
            
#         prev = list1
#         curr1 = list1.next
#         curr2 = list2
#         # for i in range(2):
#         while curr1 and curr2:
#             # print(f'prev: {_print_ll(prev)}')
#             # print(f'list1: {_print_ll(list1)}')
#             # print(f'curr1: {_print_ll(curr1)}')
#             # print(f'curr2: {_print_ll(curr2)}')
#             if curr1.val >= curr2.val: # insert curr2
#                 temp = curr2.next
#                 prev.next = curr2
#                 curr2.next = curr1
#                 prev = prev.next
#                 curr2 = temp
#             else: # curr1.val <= curr2.val
#                 curr1 = curr1.next
#                 prev = prev.next
#             # print(f'new prev: {_print_ll(prev)}')
#             # print(f'new list1: {_print_ll(list1)}')
#             # print(f'new curr1: {_print_ll(curr1)}')
#             # print(f'new curr2: {_print_ll(curr2)}')
#             # print()
#         if curr2:
#             if curr1:
#                 curr1.next = curr2
#             else:
#                 prev.next = curr2
#         return list1
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1 is None:
#             return list2
#         if list2 is None:
#             return list1
#         return self.mergeHelper(list1, list2) if list1.val <= list2.val else self.mergeHelper(list2, list1)

# # 1 -> 1 -> 3 -> 5
# # temp 2 -> 4
# # 1 -> 3 -> 5

