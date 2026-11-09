class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = 0
        third = len(nums) - 1

        while third - first > 1:
            # print(nums[first:third+1])
            second = (first + third) // 2
            if nums[first] > nums[second]: # answer in between first and second inclusive
                third = second
            elif nums[second] > nums[first] and nums[third] > nums[second]: # answer in between first and second inclusive
                third = second
            elif nums[second] > nums[first] and nums[first] > nums[third]: # answer in second and third inclusive
                first = second
        # print(f'final: {nums[first:third]}')
        return min(nums[first:third+1])
                


# 1 2 3 4 5 6 7 8 9 case 2 v
# 2 3 4 5 6 7 8 9 1 case 3 v
# 3 4 5 6 7 8 9 1 2 case 3 v
# 4 5 6 7 8 9 1 2 3 case 3 v
# 5 6 7 8 9 1 2 3 4 case 3 v
# 6 7 8 9 1 2 3 4 5 case 1 v
# 7 8 9 1 2 3 4 5 6 case 1 v
# 8 9 1 2 3 4 5 6 7 case 1 v
# 9 1 2 3 4 5 6 7 8 case 1 v


            


