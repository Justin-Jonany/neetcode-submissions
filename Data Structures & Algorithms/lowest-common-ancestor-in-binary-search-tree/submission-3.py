# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # since it's a bst then once we find a root that splits p and q then that's the ancestor. i.e. a node n s.t. p<= n <= q. because p will be left of n and q will be right of n, so there's lower common ancesotr
        if (p.val <= root.val and q.val >= root.val) or (q.val <= root.val and p.val >= root.val):
            return root
        elif (p.val <= root.val): # then q.val <= root.val as well
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


