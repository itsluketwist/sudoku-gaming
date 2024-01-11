from itertools import product
from random import sample

from sudoku_gaming.sudoku import Sudoku, SudokuBoard


def generate(difficulty: int = 5) -> Sudoku:
    """
    Randomly generate a sudoku puzzle of the chosen difficulty rating.

    Parameters
    ----------
    difficulty: int = 5
        Scale of 1 to 9, indicating how much of the board is already filled in.
        Defaults to 5 (medium difficulty).

    Returns
    -------
    Sudoku
        A valid, unsolved, Sudoku puzzle.
    """
    # ensure difficulty is between 1 and 9
    if difficulty < 1:
        difficulty = 1
    elif difficulty > 9:
        difficulty = 9

    # use the solver to generate a valid sudoku
    sudoku = Sudoku()
    assert sudoku.solved is not None
    sudoku._board = sudoku.solved

    # use the provided difficulty to calculate how many cells to clear
    num_to_clear = 72 - int(63 * ((9 - difficulty) / 8))

    # choose them randomly, and set to 0
    all_cells = list(product(range(1, 10), range(1, 10)))
    cells_to_clear = sample(all_cells, num_to_clear)
    for (x, y) in cells_to_clear:
        sudoku.set(x, y, 0)

    sudoku._original = sudoku.board  # reset the original

    return Sudoku(sudoku.board)


def solve(sudoku: Sudoku | SudokuBoard | str) -> Sudoku | None:
    """
    Solve the provided Sudoku puzzle.

    Parameters
    ----------
    sudoku: Sudoku | SudokuBoard | str
        A sudoku puzzle in any of the supported formats.

    Returns
    -------
    Sudoku | None
        A Sudoku object, containing the original puzzle and the solution, if one exists.
    """
    # before solving, wrap the puzzle in the Sudoku class and check it's valid
    if not isinstance(sudoku, Sudoku):
        sudoku = Sudoku(sudoku)

    # try to solve, and return
    sudoku.solve_original()
    return sudoku
