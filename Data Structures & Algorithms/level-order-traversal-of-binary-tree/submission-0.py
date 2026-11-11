# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. while loop and traverse the tree with bfs while updating the list
        # 2. with bfs we explore the nodes per level, so then we can put all the nodes that we explore in a list
        # runtime: O(n) O(n)
        result = []
        if root is None:
            return result
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

# [1,2,3,4,5,6,7]
# queue []
# level [4, 5, 6, 7]
# result = [[1], [2, 3], [4, 5, 6, 7]]