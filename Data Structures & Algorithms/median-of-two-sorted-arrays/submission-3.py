class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left1, right1 = 0, len(nums1) - 1
        left2, right2 = 0, len(nums2) - 1

        # for i in range(5):

        def median(nums: List[int]) -> float:
            if len(nums) % 2 == 0:
                return (nums[(len(nums) // 2)] + nums[(len(nums) // 2) - 1]) / 2
            else:
                return nums[len(nums) // 2]
                
        while (right1 - left1) > 2 and (right2 - left2) > 2:
            mid1 = (left1 + right1) // 2
            mid2 = (left2 + right2) // 2
            median1 = median(nums1[left1:right1+1])
            median2 = median(nums2[left2:right2+1])
            # print(f'before: median1 is {median1} and median2 is {median2}')
            # print(nums1[left1: right1+1])
            # print(nums2[left2: right2+1])

            if median1 == median2:
                return median1
            if median1 > median2:
                right1 = mid1
                left2 = mid2 + 1 if (right2 - left2 + 1) % 2 == 0 else mid2
            else:
                left1 = mid1 + 1 if (right1 - left1 + 1) % 2 == 0 else mid1
                right2 = mid2
            # print('after: ')
            # print(nums1[left1: right1+1])
            # print(nums2[left2: right2+1])
            # print()

            
        total = right1 +- left1 + right2 - left2 + 2 # max is 4
        nums = sorted(nums1[left1: right1 + 1] + nums2[left2: right2 + 1])
        print(nums)
        return median(nums)

# [1 3    8 9 12       19]
# [   4 7        13 18 19 20]

# mid1, mid2 =  8, 13
# right of mid 1 and left mid 2 inclusive
# [   8 9 12   19]   
# [4 7      13]   
# mid1, mid2 =  9, 7
# [8 9]
# [7 13]
# get the mid 2



# [1 3    8 9 12       19]
# [   4 7        13 18 19]
# odd
# mid1, mid2 =  8, 13
# [8 9 12 19]   [4 7 13]
# mid1, mid2 =  8, 13


        