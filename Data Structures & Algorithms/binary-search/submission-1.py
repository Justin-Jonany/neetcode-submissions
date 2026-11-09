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

# [-1,0,2,4,6,8]
# left = 0 right = 5 mid = 2 [-1,0,2,4,6,8]
# left = 3 right = 5 mid = 4 [4,6,8]
# left = 3 right = 3 mid = 4 [4]