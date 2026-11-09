# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)
        root.left = inverted_right
        root.right = inverted_left
        return root
        


        # so the task i have to do is swap every left and right child. the child follows the parent
        # 1. iterate from root
        # 2. in each depth, swap the children and use recursion to invert it.
        # 3. base case is if it's jsut itself or is empty which it's jsut return itself