class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row checks:
        print('row check')
        for row in board:
            seen = set()
            for num in row:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
        
        # column checks
        print('column check')
        for index in range(9):
            seen = set()
            for row in board:
                element = row[index]
                if element != '.':
                    if element in seen:
                        return False
                    seen.add(element)

        # 3 x 3 checks
        print('3 x 3 check')
        NUM_BOXES = 9
        for box_num in range(NUM_BOXES):
            seen = set()
            for row_index in range(3):
                for column_index in range(3):
                    row = (box_num // 3) * 3 + row_index
                    col = (box_num % 3) * 3 + column_index
                    print((row, col))
                    element = board[row][col]
                    if element != '.':
                        if element in seen:
                            return False
                        seen.add(element)
            print()
                    
        return True
