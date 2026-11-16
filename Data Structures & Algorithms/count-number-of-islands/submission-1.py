class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        num_islands = 0
        def dfs(row: int, col: int):
            if row < 0 or row >= len(grid) or 0 > col or col >= len(grid[0]):
                return
            elif grid[row][col] == "1": # Continue exploring
                grid[row][col] = "#"
            else: # either an existing island or just water
                return
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        # print(f'start: ')
        # for i in grid:
        #     print(i)
        # print()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # print((row, col))
                if grid[row][col] == "1": # didnt go through on the first condition, so this is a new isalnd
                    # print(f'island at {(row, col)}')
                    num_islands += 1
                    dfs(row, col)
                    # for i in grid:
                    #     print(i)
                    # print()
        return num_islands
                
        # iterate from left to right, top to bottom.
        # for each island we check if any of NSWE are water.
            # If we only add num_islands + 1 if all is water. Then everything will be 0
            # What if we only check the directions we are iterating from so we only update +1 on the first apperance?
                # only plus one if east and north is water. this will fail if we have a horizontall flipped L shape. like in example 1. we weill plus one at (0, 1) and (2, 0). 
            # what if we mark discovered islands as True, and then once we see an island, we will do num_islands + 1 and iterate to all paths and mark all true. Then after we continue iterating the grid and when we find an island that is not marked true yet, we do num_islands + 1, and then iterate again. This would be O(mn). space is not O(1) despite in place because of recursion stack. it's O(mn as well.