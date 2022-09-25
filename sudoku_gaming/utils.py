from random import shuffle
from typing import Optional

from .sudoku import Sudoku


def _find_possible_values(sudoku: Sudoku, row: int, col: int):
    """
    Utility function to find the possible values for a cell in a sudoku puzzle.

    Parameters
    ----------
    sudoku : Sudoku
    row : integer
    col : integer

    Returns
    -------
    List[int]
        All possible values for the given cell in the Sudoku.
        List is empty if cell is not blank.
    """
    # no possible values if cell is not blank
    if sudoku.get(row, col) != 0:
        return []

    # find the numbers already in the same row / column
    row_nums = {sudoku.get(row, y) for y in range(9)} - {0}
    col_nums = {sudoku.get(x, col) for x in range(9)} - {0}

    # find the numbers for the cell's local 3x3 grid
    grid_nums = set()
    x_start = (row // 3) * 3
    y_start = (col // 3) * 3

    # loop over the grid, finding it's contained numbers
    for x in range(x_start, x_start + 3):
        for y in range(y_start, y_start + 3):
            if sudoku.get(x, y) != 0:
                grid_nums.add(sudoku.get(x, y))

    # determin the possible values and return
    sudoku_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    possible_nums = sudoku_nums - (row_nums | col_nums | grid_nums)
    return list(possible_nums)


def _recursive_solve(sudoku: Sudoku) -> Optional[Sudoku]:
    """
    Solves a Sudoku puzzle recursively, using a depth-first backtracking
    algorithm. Each blank cell will be filled in order of which has the least
    possible values first.

    Parameters
    ----------
    sudoku : Sudoku

    Returns
    -------
    Optional[Sudoku]
        Return the solution if one is found, otherwise None.
    """
    empty_cells = []  # initialise list

    # find all non-zero cells
    for x in range(9):
        for y in range(9):
            if sudoku.get(x, y) == 0:
                empty_cells.append((x, y, _find_possible_values(sudoku, x, y)))

    # sort cells in order of which has the least possible values
    empty_cells.sort(key=lambda blank: len(blank[2]))

    for (i, j, possible) in empty_cells:
        if sudoku.get(i, j) == 0:
            shuffle(possible)
            for p in possible:
                # enter possible value in the cell, and try to solve
                sudoku.set(i, j, p)
                solution = _recursive_solve(sudoku)

                # return solution if found
                if solution is not None:
                    return solution

            # no valid non-zero value for cell, reset and return
            sudoku.set(i, j, 0)
            return None

    # if no empty cell is found, sudoku must be complete
    return sudoku
