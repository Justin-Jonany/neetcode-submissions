# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def string_ll(t):
            s = ""
            seen = set()
            while t:
                # if t in seen:
                #     print('LOOP')
                #     break
                seen.add(t)
                s += f"{t.val}->"
                t = t.next
            return s
        print(string_ll(head))
        print(string_ll(slow))
        print()
        reverse_start = slow.next   # second half starts after slow
        prev = slow.next = None     # cut the first half; prev starts at None
        while reverse_start:
            temp = reverse_start.next
            reverse_start.next = prev
            prev = reverse_start
            reverse_start = temp
        
        print(string_ll(head))
        print(string_ll(prev))
        print()

        # so now the reversed list is at prev
        # and the other list is from head to slow inclusive. if it's even we want to icnldue it, otherwise if it's odd, no
        # now we merge it alternatingly

        print(f'head: {string_ll(head)}')
        print(f'prev: {string_ll(prev)}')
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        # second.next = None

        # 2->10->4->8-> 6
        # 10->8->6->
        # first1 4->6->
        # first2 8->6->
        # tmp1 6->
        # tmp2  6->





    # 2 -> 3 -> 4
    # temp None
    # prev 4 -> 3 -> 2 -> None
    # reverse_start None






        # O(n) space
        # stack = []
        # curr = head
        # while curr:
        #     stack.append(curr)
        #     curr = curr.next

        # i, j = 0, len(stack) - 1
        # while i < j:
        #     stack[i].next = stack[j]
        #     stack[j].next = stack[i+1]
        #     i += 1
        #     j -= 1
        # stack[i].next = None
        
        


# 2 -> 4 -> 6 -> 8 -> 10
# 2 4 6 v
# 2 6 10

# 2 -> 4 -> 6 -> 8
# 6
# None


