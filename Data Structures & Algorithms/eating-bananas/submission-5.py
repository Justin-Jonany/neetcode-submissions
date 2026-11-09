import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        if len(piles) == 1:
            return math.ceil(piles[0] / h)

        def _hours_needed(piles: List[int], k: int) -> int:
            return sum([math.ceil(p/k) for p in piles])
        lowest = high # assumes enough hour
        while low <= high:
            mid = (high + low) // 2
            # print(f'{(low, high)} mid is {mid}: {_hours_needed(piles, mid)}')
            if _hours_needed(piles, mid) <= h: # rate can go lower. their may be multiple k that has the same h, so need get the lower one.
                high = mid-1
                lowest = min(lowest, mid)
            elif _hours_needed(piles, mid) > h: # rate is too low
                low = mid+1
            # else: # if it's equal already, if we make it lwoer it will go over h
            #     return mid
        return lowest
            
        





# [1,4,3,2]
# [1, 2, 3, 4]
# k = max = 4  < 9 yes

# k = 2 < yes

# k = 1 > no