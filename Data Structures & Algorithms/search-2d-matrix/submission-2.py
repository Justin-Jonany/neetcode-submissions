class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        def _to_coordinates(i: int) -> (int, int):
            return (i // len(matrix[0]), i % len(matrix[0]))
        # print(f'3: {_to_coordinates(3)}')
        # print(f'8: {_to_coordinates(8)}')
        # print(f'{right}: {_to_coordinates(right)}')
        while left <= right:
        # for _ in range(5):
            mid = (left + right) // 2
            row, col = _to_coordinates(mid)
            left_coord = _to_coordinates(left)
            right_coord = _to_coordinates(right)
            # print(f'left ({left}): {left_coord}  right ({right}): {right_coord} mid: {mid} {(row, col)}')
            # print(f'{matrix[row][col]}')
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        # print()
        return False