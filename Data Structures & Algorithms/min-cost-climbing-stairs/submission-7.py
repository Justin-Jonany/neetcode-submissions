class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] = cost of combing to the top from index i
        # at index n-1 and n-2, that's just their cost directly
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
            # print(table)
        # we can start from index 0 or 1
        return min(cost[0], cost[1])
        
        # table = [0 for _ in range(len(cost) + 1)]
        # table = [0 for _ in range(3)]

        # for i in range(2, len(cost) + 1):
        #     table[i % 3] = min(cost[(i-2)] + table[(i-2) % 3], cost[(i-1)] + table[(i-1) % 3])
        #     # print(table)
        # return table[len(cost) % 3]

        # create every possible path
            # at each index have two directions. depth is at most n, take one step at at ime. so run time is 2^n
        # dynamic programming
            # with a 1D array save the min cost of climbing the stairs up to that point
            # T[0] = 0
            # T[1] = 0
            # T[2] = Min(T[0] + cost[0], T[0] + cost[1])
            # T[3] = Min(T[1] + cost[1], T[2] + cost[2])
        


# Input: cost = [1,2,3]
# Output: 2

# T[i] = the minimum cost of climbing stairs to reach index i. 
# Table = [0 0 1 2]
# T[2] = Min(T[0] + cost[0], T[1] + cost[1])
# T[3] = Min(T[1] + cost[1], T[2] + cost[2]) = Min(0 + 2, 1 + 3)
# T[i] = Min(T[i-2] + cost[i-2], T[i-1] + cost[i-1])
# O(n) space and runtime
