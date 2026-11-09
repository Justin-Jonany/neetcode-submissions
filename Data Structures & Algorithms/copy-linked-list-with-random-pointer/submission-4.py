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
        curr = newHead
        seen = {None: None, head: newHead}
        while head:
            if head.next in seen:
                curr.next = seen[head.next]
            else:
                curr.next = Node(head.next.val)
                seen[head.next] = curr.next

            if head.random in seen:
                curr.random = seen[head.random]
            else:
                curr.random = Node(head.random.val if head.random else head.random)
                seen[head.random] = curr.random

                
            curr = curr.next
            head = head.next
        return newHead

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
        