# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            # print(f'p: {[(n.val if n else "Null") for n in stack_p]}')
            # print(f'q: {[(n.val if n else "Null") for n in stack_q]}')
            # print()
            curr_p, curr_q = stack_p.pop(), stack_q.pop()
            if curr_p and curr_q:
                if curr_p.val != curr_q.val:
                    return False
                stack_p.append(curr_p.left)
                stack_p.append(curr_p.right)
                stack_q.append(curr_q.left)
                stack_q.append(curr_q.right)
            elif curr_p or curr_q: # one of them is null and the other is not null
                return False
            # else both are null and nothing happens
        return True


        # have two pointers, iterating with the same search algo (im gonna use dfs) and anytime value is different or one is null when the other isn't, return False