class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        third = len(nums) - 1

        i = 0
        while third - first > 1:
            second = (first + third) // 2
            if nums[first] == target:
                return first
            if nums[second] == target:
                return second
            if nums[third] == target:
                return third
            
            if nums[first] < nums[second] < nums[third]:
                if nums[second] < target:
                    first = second + 1
                else:
                    third = second - 1
            elif nums[first] < nums[second]  and nums[second] > nums[third]:
                if nums[first] < target < nums[second]:
                    third = second - 1
                else:
                    first = second + 1
            elif nums[first] > nums[second] > nums[third]:
                if nums[second] < target:
                    third = second - 1
                else:
                    first = second + 1
            elif nums[first] > nums[second] < nums[third]: # 6 2 3 4 5
                if nums[second] < target < nums[third]:
                    first = second + 1
                else:
                    third = second - 1

        if nums[first] == target:
            return first
        elif nums[third] == target:
            return third
        else:
            return -1


# [3,5,6,0,1,2] target = 5
# first < second < third
# first < second > third 4 5 6 2 3
# first > second > third 
# first > second < third 6 7 3 4 5

# 6 5 4 3 2 1 0

