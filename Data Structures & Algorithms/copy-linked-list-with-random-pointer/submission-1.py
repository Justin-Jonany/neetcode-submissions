"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        newHead = Node(head.val)
        pointer = newHead
        seen = {head: newHead}
        while head:
            if head.next and head.next in seen:
                newHead.next = seen[head.next]
            elif head.next:
                newHead.next = Node(head.next.val)
                seen[head.next] = newHead.next
            else:
                newHead.next =  head.next

            if head.random and head.random in seen:
                newHead.random = seen[head.random]
            elif head.random:
                newHead.random = Node(head.random.val if head.random else head.random)
                seen[head.random] = newHead.random
            else:
                newHead.random =  head.random
                
            newHead = newHead.next
            head = head.next
        return pointer

# original [[3,null],[7,3],[4,0],[5,1]]
# copied [3, null] -> [7, 3] -> [4, 0] -> [5, null] -> 
# newHead [5, 1]
# seen {original 3: new 3, original 7: new 7, original 4: new 4, original 5: new 5}
# head [5, 1]


# 1. new dummy head 0
# 2. hashmap key address and the value is the node object
# 3. iterate through head
#     a. check in hashmap if it already exist
#     b. if yes
#         c. grab it (fix it later when i write code)
#         d. want to assign the .next
#             e. check in hashmap
#                 f. if not yet exist create, otehrwise. just use the eixsitng one
#             f. same thing with random
#     c. if no
        