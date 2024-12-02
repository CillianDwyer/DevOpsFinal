def is_valid_board(board):
    if len(board) != 9:
        raise ValueError("Board must have 9 rows")
    for row in board:
        if len(row) != 9:
            raise ValueError("Each row must have 9 columns")
        for num in row:
            if num < 0 or num > 9:
                raise ValueError("Board values must be between 0 and 9")
            if not isinstance(num, int):
                raise ValueError("Board values must be integers")
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return board
                        board[row][col] = 0
                return None  # No valid number can be placed, return None
    return board  # Board is solved
