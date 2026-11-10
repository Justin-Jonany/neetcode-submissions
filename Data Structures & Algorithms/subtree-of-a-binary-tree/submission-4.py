# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    # O(min(n,m)) where n is number of ndoes of tree2 m is number of ndoes of tree2 (subtree) because it will stop if one of them runs out of nodes to traverse
    def sameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode])->bool:
        if tree1 is None and tree2 is None:
            return True
        if tree1 and tree2:
            if tree1.val != tree2.val:
                return False
            else:
                return self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right)

        return False


    # worse case for each node in root we do sameTree. O(n * min(n,m)) and space is O(h_1) where h1 is height of root since worst case is we recurse to the deepest node in root. sameTree is boudned by wichever is smaller between height of root and subroot. 
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

