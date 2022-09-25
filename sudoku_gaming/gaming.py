from itertools import product
from random import sample
from typing import Optional, Union

from .sudoku import Sudoku, SudokuBoard
from .utils import _recursive_solve


def generate(difficulty: int = 5) -> Sudoku:
    """
    Randomly generate a sudoku puzzle of the chosen difficulty rating.

    Parameters
    ----------
    difficulty : int
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
    sudoku = _recursive_solve(Sudoku())
    assert sudoku is not None  # to satisfy mypy, by definition can't be None

    # use the provided difficulty to calculate how many cells to clear
    num_to_clear = 72 - int(63 * ((9 - difficulty) / 8))

    # choose them randomly, and set to 0
    all_cells = list(product(range(9), range(9)))
    cells_to_clear = sample(all_cells, num_to_clear)
    for (x, y) in cells_to_clear:
        sudoku.set(x, y, 0)

    return Sudoku(sudoku.board)


def solve(sudoku: Union[Sudoku, SudokuBoard, str]) -> Optional[Sudoku]:
    """
    Solve the provided Sudoku puzzle.

    Parameters
    ----------
    sudoku : Union[Sudoku, SudokuBoard, str]
        A sudoku puzzle in any of the supported formats.

    Returns
    -------
    Optional[Sudoku]
        The solved Sudoku, if a solution exists, otherwise None.
    """
    # before solving, wrap the puzzle in the Sudoku class and check it's valid
    if not isinstance(sudoku, Sudoku):
        sudoku = Sudoku(sudoku)

    # try to find the solution
    return _recursive_solve(sudoku)


def play(sudoku: Union[Sudoku, SudokuBoard, str]) -> Sudoku:
    """
    Play a game of sudoku!

    Parameters
    ----------
    sudoku : Union[Sudoku, SudokuBoard, str]
        A sudoku puzzle in any of the supported formats.

    Returns
    -------
        The current state of the Sudoku when ending the play session.
    """
    # before playing, wrap the puzzle in the Sudoku class and check it's valid
    if not isinstance(sudoku, Sudoku):
        sudoku = Sudoku(sudoku)

    raise NotImplementedError("The play method is not yet implemented...")
