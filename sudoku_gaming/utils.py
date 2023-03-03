from random import shuffle
from typing import Optional

from sudoku_gaming.types import SudokuBoard


def _board_string(board: SudokuBoard, title: str = "Sudoku") -> str:
    """
    Get a printable string representation of a SudokuBoard.

    Parameters
    ----------
    board : SudokuBoard
    title : str

    Returns
    -------
    str
        A printable string representation of the given sudoku board.
    """
    return (
        f"\n{title}:\n"
        + "\n".join([" ".join([str(n) for n in row]) for row in board])
        + "\n"
    )


def _find_possible_values(sudoku: SudokuBoard, row: int, col: int):
    """
    Utility function to find the possible values for a cell in a sudoku puzzle.

    Parameters
    ----------
    sudoku : SudokuBoard
    row : integer
    col : integer

    Returns
    -------
    List[int]
        All possible values for the given cell in the Sudoku.
        List is empty if cell is not blank.
    """
    # no possible values if cell is not blank
    if sudoku[row][col] != 0:
        return []

    # find the numbers already in the same row / column
    row_nums = {sudoku[row][y] for y in range(9)} - {0}
    col_nums = {sudoku[x][col] for x in range(9)} - {0}

    # find the numbers for the cell's local 3x3 grid
    grid_nums = set()
    x_start = (row // 3) * 3
    y_start = (col // 3) * 3

    # loop over the grid, finding it's contained numbers
    for x in range(x_start, x_start + 3):
        for y in range(y_start, y_start + 3):
            if sudoku[x][y] != 0:
                grid_nums.add(sudoku[x][y])

    # determine the possible values and return
    sudoku_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    possible_nums = sudoku_nums - (row_nums | col_nums | grid_nums)
    return list(possible_nums)


def _check_for_duplicates(board: SudokuBoard) -> bool:
    """
    Check for duplicate numbers in each row, column and grid of the sudoku board.

    Parameters
    ----------
    board : SudokuBoard
        The sudoku board to check.

    Returns
    -------
    bool
        True if duplicates are found, False otherwise.
    """
    # first check the rows and columns for their non-zero entries
    for index in range(9):
        row_nums = [board[index][y] for y in range(9) if board[index][y] != 0]
        col_nums = [board[x][index] for x in range(9) if board[x][index] != 0]

        # check for duplicates by comparing list size to set size
        if len(row_nums) != len(set(row_nums)):
            return True
        if len(col_nums) != len(set(col_nums)):
            return True

    # now loop over each grid, checking for duplicates
    for x_start in [0, 3, 6]:
        for y_start in [0, 3, 6]:
            grid_nums = set()
            for x in range(x_start, x_start + 3):
                for y in range(y_start, y_start + 3):

                    # non-zero entries already seen are duplicates
                    num = board[x][y]
                    if num != 0 and num in grid_nums:
                        return True
                    else:
                        grid_nums.add(num)

    # no duplicates found
    return False


def _recursive_solve(sudoku: SudokuBoard) -> Optional[SudokuBoard]:
    """
    Solves a Sudoku puzzle recursively, using a depth-first backtracking
    algorithm. Each blank cell will be filled in order of which has the least
    possible values first.

    Parameters
    ----------
    sudoku : SudokuBoard

    Returns
    -------
    Optional[Sudoku]
        Return the solution if one is found, otherwise None.
    """
    empty_cells = []  # initialise list

    # find all non-zero cells
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                empty_cells.append((x, y, _find_possible_values(sudoku, x, y)))

    # sort cells in order of which has the least possible values
    empty_cells.sort(key=lambda blank: len(blank[2]))

    for (i, j, possible) in empty_cells:
        if sudoku[i][j] == 0:
            shuffle(possible)
            for p in possible:
                # enter possible value in the cell, and try to solve
                sudoku[i][j] = p
                solution = _recursive_solve(sudoku)

                # return solution if found
                if solution is not None:
                    return solution

            # no valid non-zero value for cell, reset and return
            sudoku[i][j] = 0
            return None

    # if no empty cell is found, sudoku must be complete
    return sudoku
