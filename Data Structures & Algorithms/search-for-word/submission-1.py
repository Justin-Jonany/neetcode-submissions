class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        seen = [[False for _ in row] for row in board]
        word_queue = deque(word)
        def dfs(path: list[tuple(int, int)]) -> bool:
            if len(word_queue) == 0:
                return True

            last_cell = path[-1]

            # a position is (x, y)
            moves = []
            if last_cell[0] > 0:
                moves.append((last_cell[0] - 1, last_cell[1]))
            if last_cell[0] < len(board) - 1:
                moves.append((last_cell[0] + 1, last_cell[1]))
            if last_cell[1] < len(board[0]) - 1:
                moves.append((last_cell[0], last_cell[1] + 1)) 
            if last_cell[1] > 0:
                moves.append((last_cell[0], last_cell[1] - 1)) 

            for move in moves:
                if (not seen[move[0]][move[1]]) and (board[move[0]][move[1]] == word_queue[0]):
                    path.append(move)
                    word_queue.popleft()
                    seen[move[0]][move[1]] = True
                    if dfs(path):
                        return True
                    seen[move[0]][move[1]] = False
                    path.pop()
                    word_queue.appendleft(board[move[0]][move[1]])
            return False
                    

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    p = [(i, j)]
                    seen[i][j] = True
                    word_queue.popleft()
                    if dfs(p):
                        return True
                    p = []
                    seen[i][j] = False
                    word_queue.appendleft(board[i][j])
        return False
                    
        


        # backtracking
        # two for loops iterating from left to right top to bottom
            # when it sees the letter that matches the first letter of the word
            # dfs recursion and traverses to top, left, right, or bottom if the next letter is there. otherwise return false.
                # seen array and recursion carries the path
            # once it finds a path return bool

        # each cell have four moves. branching factor is four. depth n*m. 4 ^(n*m)runtime. and the space complexity is just the n*m. 

            