# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_prev, l1_pointer = None, l1
        l2_pointer = l2

        add1 = False
        while l1_pointer and l2_pointer:
            res = l1_pointer.val + l2_pointer.val 
            if add1:
                res += 1
                add1 = False
            if res >= 10:
                add1=True
            remainder = res % 10

            l1_prev= l1_pointer
            l1_pointer.val = remainder
            l1_pointer = l1_pointer.next
            l2_pointer = l2_pointer.next
        
        while l2_pointer:
            if add1:
                l2_pointer.val += 1
                add1 = False
            if l2_pointer.val >= 10:
                add1 = True
            l2_pointer.val = l2_pointer.val % 10
            l1_prev.next = l2_pointer
            l2_pointer = l2_pointer.next
            l1_prev = l1_prev.next

        while l1_pointer:
            if add1:
                l1_pointer.val += 1
                add1 = False
            if l1_pointer.val >= 10:
                add1 = True
            l1_pointer.val = l1_pointer.val % 10
            l1_prev = l1_pointer
            l1_pointer = l1_pointer.next
        
        if add1:
            l1_prev.next = ListNode(1)


        return l1





        # [9, 9]
        # [9]
        # 99 + 9 =  108
        # result(l1) [8, 9]
        # add1 = True
        # l1_prev 9
        # res = 18
        # remainder =  8
        # l1_pointer 9
        # l2_pointer 9

        # 1. two pointers one for each list
        # 2. add the values and modify l1. we use mod, adn the remaidner we overwrrite l1. and then if it's over 10 we have a variable that will add 1 to the next iteratin
        # 3. move the two poitners
        
        # edges cases:
        # 1. if one of them is already empty and the other one still has item. (this can be from the beginning like if oe ofhtem is None)
        #     2. then we just create new nodes if l2 is longer since we are overwriting l1.
        #     3. return l1 and dont forget to add 1 from the final iteration if needed.