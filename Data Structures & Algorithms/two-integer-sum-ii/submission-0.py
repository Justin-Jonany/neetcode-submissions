class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since we must do O(1) additional space, then we cannot create
        # a hash set because that will make it O(n)
        # so only one pass? maybe some vars on the side
        first = 0
        last = len(numbers) - 1

        while True:
            curr = numbers[first] + numbers[last]
            if curr == target:
                return [first + 1, last + 1]
            elif target > curr:
                first += 1
            elif target < curr:
                last -= 1
