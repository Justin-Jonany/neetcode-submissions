class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        # heapq.heapify(self.heap)
        for i in range(min(k, len(nums))):
            heapq.heappush(self.heap, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > self.heap[0]:
                heapq.heappushpop(self.heap, nums[i])


# ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [2], "add", [4]]
# heap = [3, 3, 4]    
# 3 3 3


    def add(self, val: int) -> int:
        if self.k > len(self.heap):
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        
# to get largest k in a dynamic array without consistently looking at all the n iterations.
# when we initialize it:
    # if we use a list it means that to find the kth largest after creating the list would be O(n^2)
    # create a min heap with only the kth largest, so the kth largest is in the root. we iterate through nums and when we have k items, we start filtering. if the next num is larger than the min (root), then we remove root O(1) and push the num O(logk). do this for all n items and that's O(nlogk)

# when we add:
    # if it's smaller or euql to the kth largest we have stored. we dont do anything and jsut return the kth alrgest.
    # if it's larger tho, then we have to remove root, and push the new value O(logk)
