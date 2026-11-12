class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)): # O(n) to turn it to max heap
            nums[i] = nums[i] * -1
        heapq.heapify(nums) # # O(n)
        for _ in range(k - 1): # O (k - 1)
            heapq.heappop(nums)
        return nums[0] * -1

        # memory is O(1) since it's in place. runtime is O(n) to heapify it. 
