# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def helper(root: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            diameter = 0
            if root is None:
                return diameter
            left = helper(root.left)
            right = helper(root.right)

            if root.left:
                left += 1
            if root.right:
                right += 1
            max_diameter = max(max_diameter, left + right)
            return max(left, right)
        helper(root)
        return max_diameter

        # count the left and count the right then add them together