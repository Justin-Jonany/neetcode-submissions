class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # print(f'{(left, right)} search area: {nums[left: right + 1]} \t\tmid ({mid}): {nums[mid]}')
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: # answer is on the left
                right = mid - 1
            else: # answer is on the right
                left = mid + 1
        return -1