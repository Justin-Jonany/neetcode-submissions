# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    max_count = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if root is None:
            return count
        # print(f'{root.val} count {count}')
        left_count = self.maxDepth(root.left)
        right_count = self.maxDepth(root.right)
        count = max(left_count, right_count) + 1
        self.max_count = max(self.max_count, count)
        # print(f'\t{root.val} count {count}')
        return count
            
