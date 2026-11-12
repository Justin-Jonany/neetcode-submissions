class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k 
        # [1, 2, 3, 4, 5] k = 2, answer is 4. index 3. so len(nums) - k = 5 - 2 = 3
        def quickselect(l: int, r: int) -> int:
            pivot, curr = nums[r], l
            for i in range(l, r): # no + 1 because the last item is the pivot
                if nums[i] < pivot:
                    nums[i], nums[curr] = nums[curr], nums[i]
                    curr += 1
            nums[r], nums[curr] = nums[curr], nums[r]

            # now the pivot is in the ocrrect position, index curr
            # left of it is smaller, and right of it is larger

            if curr > k:
                return quickselect(l, curr - 1)
            elif curr < k:
                return quickselect(curr + 1, r)
            else:
                return nums[curr]

        return quickselect(0, len(nums) - 1)



        # for i in range(len(nums)): # O(n) to turn it to max heap
        #     nums[i] = nums[i] * -1
        # heapq.heapify(nums) # # O(n)
        # for _ in range(k - 1): # O (k - 1 logn)
        #     heapq.heappop(nums)
        # return nums[0] * -1

        # # memory is O(1) since it's in place. runtime is O(klogn) to heapify it. 
