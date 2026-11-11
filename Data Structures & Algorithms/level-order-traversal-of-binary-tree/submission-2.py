# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # recursion helper with extra param level and local result
        # at each node, append the node into the array at index level, if doesnt exist create list
        result = []
        def dfs(root: Optional[TreeNode], level: int):
            nonlocal result
            # print(f'{root.val if root else "None"} level {level}: {result}')
            if root is None:
                return

            level += 1
            if len(result) < level:
                result.append([])
            result[level - 1].append(root.val)

            dfs(root.left, level)
            dfs(root.right, level)
            # level -= 1
        dfs(root, 0)
        return result

# [1,2,3]
# root = 3
# level = 1
# result = [[1], [2, 3]]

        # # 1. while loop and traverse the tree with bfs while updating the list
        # # 2. with bfs we explore the nodes per level, so then we can put all the nodes that we explore in a list
        # # runtime: O(n) O(n)
        # result = []
        # if root is None:
        #     return result
        # queue = deque([root])
        # while queue:
        #     level = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     result.append(level)
        # return result

# [1,2,3,4,5,6,7]
# queue []
# level [4, 5, 6, 7]
# result = [[1], [2, 3], [4, 5, 6, 7]]