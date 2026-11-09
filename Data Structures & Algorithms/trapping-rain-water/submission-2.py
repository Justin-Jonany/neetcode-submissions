class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        water = 0

        left_peak_height = height[left]
        right_peak_height = height[right]

        while left < right:
        # for i in range(3):
            # print(f'{(left, right)}')
            # finds first left peak or replaces the current peak when it finds another index with the same or a larger index
            while (
                left < right and 
                height[left+1] >= left_peak_height
            ):
                left += 1
                left_peak_height = height[left]
            while (
                left < right and 
                height[right - 1] >= right_peak_height
            ):

                right -= 1
                right_peak_height = height[right]

            if left == right:
                break

            # print(f'\tleft_peak_height: {left_peak_height}, right_peak_height: {right_peak_height}')

            if left_peak_height < right_peak_height:
                left += 1
                water += left_peak_height - height[left]
                # print(f'\tleft adding at {left} by {left_peak_height - height[left]}')
            else:
                right -= 1
                water += right_peak_height - height[right]
                # print(f'\tright adding at {right} by {right_peak_height - height[right]}')
        return water


