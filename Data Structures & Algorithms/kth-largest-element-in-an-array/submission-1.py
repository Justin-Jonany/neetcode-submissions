class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)): # O(n) to turn it to max heap
            nums[i] = nums[i] * -1
        heapq.heapify(nums) # # O(n)
        for _ in range(k - 1): # O (k - 1)
            heapq.heappop(nums)
        return nums[0] * -1