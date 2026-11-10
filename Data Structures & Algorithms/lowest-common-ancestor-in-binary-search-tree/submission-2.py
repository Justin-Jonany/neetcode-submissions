# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 1. find p and q first and keeping all ancestors from before O(|v|) and keeping the level in which they were found
        # 2. then find the match in their ancestors? O(|v|)
        path_p = []
        path_q = []

        # O(h)
        def dfs(root: TreeNode, path: list[tuple(TreeNode, int)], level: int) -> None:
            # print('->'.join([f"{n.val}" for n,_ in path] + [f"{root.val if root else 'None'}"]))
            nonlocal p, q, path_p, path_q
            if root is None:
                return
            level += 1
            path += [(root, level)]
            if root == p:
                # print(f'\tp found: ', '->'.join([f"{n.val}" for n,_ in path]))
                path_p = path.copy() # O(h) but only happens once
            if root == q:
                # print(f'\tq found: ', '->'.join([f"{n.val}" for n,_ in path]))
                path_q = path.copy() # O(h) but only happens once
            dfs(root.left, path, level)
            dfs(root.right, path, level)

            # backtrack
            path.pop()
        
        dfs(root, [], 0)

        # now path_p and path_q populated. We just need to find common ancestor
        # print()
        # print('path p: ', '->'.join([f"{n.val}" for n,_ in path_p]))
        # print('path q: ', '->'.join([f"{n.val}" for n,_ in path_q]))
        similar_ancestors = [node for node in path_p if node in path_q]
        # print('similar anc: ', '->'.join([f"{n.val}" for n,_ in similar_ancestors]))
        return max(similar_ancestors, key=lambda x: x[1])[0]
            
            

