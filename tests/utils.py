"""A collection of utiliy functions used for testing the library."""

from sudoku_gaming import SudokuBoard


def count_blanks(board: SudokuBoard) -> int:
    """
    Utility function to count the number of zeroes in a SudokuBoard.
    """
    num_zeroes = 0

    for row in board:
        for value in row:
            if value == 0:
                num_zeroes += 1

    return num_zeroes


def assert_complete_sudoku(board: SudokuBoard):
    """
    Utility function to check that a SudokuBoard has been correctly solved.
    """
    _1_to_9 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # check rows
    for row in board:
        assert set(row) == _1_to_9

    # check columns
    for i in range(9):
        assert {board[x][i] for x in range(9)} == _1_to_9

    # check grids
    for x_start in [0, 3, 6]:
        for y_start in [0, 3, 6]:
            grid_nums = {
                board[x][y]
                for x in range(x_start, x_start + 3)
                for y in range(y_start, y_start + 3)
            }
            assert grid_nums == _1_to_9
