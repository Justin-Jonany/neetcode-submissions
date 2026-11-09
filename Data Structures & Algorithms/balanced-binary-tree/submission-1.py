# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # use dfs to get count of left and right if at any point height is different more than 1 then it's not balanced
        balanced = True
        def dfs(root: Optional[Treenode]) -> bool:
            nonlocal balanced
            if root is None:
                return 0
            # print(root.val)
            left = dfs(root.left)
            right = dfs(root.right)
            # print(f'\tleft: {left}')
            # print(f'\tright: {right}')
            if abs(right-left) > 1:
                balanced = False
            return max(left, right) + 1
        dfs(root)
        return balanced