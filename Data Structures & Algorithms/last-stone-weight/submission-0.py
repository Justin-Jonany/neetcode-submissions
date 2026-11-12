class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)

        while len(stones) > 1:
            # edge case where the final two stones are equal size, then this still works
            largest, second_largest = heapq.heappop(stones) * -1, heapq.heappop(stones) * -1
            if largest > second_largest:
                heapq.heappush(stones, -1 * (largest - second_largest))
        return stones[0] * -1 if len(stones) == 1 else 0

# [1, 2, 3]
# [-1, -1]
# 1, 1
# []


        # use max heap.
        # since heapq is min heap and there's no max heap implementation, we have to set the weights to negative. O(n) we negate and heapify
        # while loop on heapq len() > 1
            # do heappop twice. and dont forget to * -1 it because we stored it in negatives.
            # we do comparisons
                # equal, just continue
                # otherwise, y-x and insert back the stone (logn)
        
        # each time, grab two max (O(1)), insert one back Ologn. do this n times. that's O(nlogn). space is O(1) because we are using the original list