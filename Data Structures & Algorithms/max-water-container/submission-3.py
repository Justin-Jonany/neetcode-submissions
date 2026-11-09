class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1. brute force: for all pairs compute the area
        # max_area = 0
        # for i in range(len(heights)):
        #     for j in range(i, len(heights)):
        #         max_area = max(max_area, (j - i) * min(heights[i], heights[j]))
        # return max_area # will timeout

        # 2. two pointers
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, area)
            # Everytime we move a pointer towards the middle, we lose the width by 1.
            # We move the one where height is min to minimize loss
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area


