# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def sameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode])->bool:
        if tree1 is None and tree2 is None:
            return True
        if tree1 and tree2:
            if tree1.val != tree2.val:
                return False
            else:
                return self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right)

        return False


            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # print(f'checking root: {root.val if root else "None"}')
        if root is None and subRoot is None:
            return True
        if root and subRoot:
            if root.val == subRoot.val:
                # print(f'\tpotential match')
                if self.sameTree(root, subRoot):
                    return True
            # if no match then check left and right child
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False

