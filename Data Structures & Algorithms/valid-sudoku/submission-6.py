class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            number_appeard = {}
            for cell in row:
                if cell != '.':
                    if cell in number_appeard: # number have been seen in the row before
                        return False
                    number_appeard[cell] = True
        
        NUM_ROW_COL_CELLS = 9
        for row in range(NUM_ROW_COL_CELLS):
            number_appeard = {}
            for col in range(NUM_ROW_COL_CELLS):
                cell = board[col][row]
                if cell != '.':
                    if cell in number_appeard: # number have been seen in the column before
                        return False
                    number_appeard[cell] = True

        # go to each boxes and iterate
        for row in range(0, NUM_ROW_COL_CELLS, 3):
            for col in range(0, NUM_ROW_COL_CELLS, 3):
                number_appeard = {}
                for square_row in range(row, row + 3):
                    for square_col in range(col, col + 3):
                        cell = board[square_row][square_col]
                        if cell != '.':
                            if cell in number_appeard: # number have been seen in the column before
                                return False
                            number_appeard[cell] = True
        return True





                
                    
            