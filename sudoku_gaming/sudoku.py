from copy import deepcopy
from typing import Optional, Union

from sudoku_gaming.types import SudokuBoard
from sudoku_gaming.utils import _board_string, _check_for_duplicates, _recursive_solve


class Sudoku:
    """
    An object representing a sudoku puzzle, containing a game board and logic
    to update the board state and display it.
    """

    def __init__(self, board: Union[SudokuBoard, str, None] = None):
        """
        Parameters
        ----------
        board : Union[SudokuBoard, str, None]
            A representation of the Sudoku board. Either:
                - 9x9 array of integers,
                - comma-separated string of the rows,
                - or None, in which case a blank puzzle is generated.
            Blank cells should be represented with a 0.
            Provided board will be validated once parsed.
        """
        self._board: SudokuBoard = [[]]
        if board is None:
            self._board = [[0 for _ in range(9)] for _ in range(9)]
        elif isinstance(board, str):
            self._board = [[int(n) for n in row] for row in board.split(",")]
        else:
            self._board = board

        self._validate()

        self._original = deepcopy(self._board)
        self._solved: Optional[SudokuBoard] = None
        self._solve_attempted = False

    def get(self, row: int, col: int) -> Optional[int]:
        """
        Return the value of a cell from the sudoku board.

        Parameters
        ----------
        row : int
            Must be a value between 1 and 9 inclusive.
        col : int
            Must be a value between 1 and 9 inclusive.

        Returns
        -------
        Optional[int]
            Will return the value of the specified cell, or None if invalid inputs were given.
        """
        # first check inputs are valid
        if (not 1 <= row <= 9) or (not 1 <= col <= 9):
            print(
                f"Error: row and col must be between 1 and 9 only (row={row}, col={col})."
            )
            return None

        return self._board[9 - row][col - 1]

    def set(self, row: int, col: int, value: int) -> None:
        """
        Update the value of a cell in the sudoku board.

        Parameters
        ----------
        row : int
            Must be a value between 1 and 9 inclusive.
        col : int
            Must be a value between 1 and 9 inclusive.
        value : int
            Must be a value between 0 and 9 inclusive (0 clears the cell).
        """
        # first check inputs are valid
        if (not 1 <= row <= 9) or (not 1 <= col <= 9):
            print(
                f"Error: row and col must be between 1 and 9 only (row={row}, col={col})."
            )
            return

        if not 0 <= value <= 9:
            print(f"Error: value must be between 0 and 9 only (value={value}).")
            return

        self._board[9 - row][col - 1] = value

    @property
    def board(self) -> SudokuBoard:
        """Getter for the current state of the sudoku board."""
        return self._board

    @property
    def original(self) -> SudokuBoard:
        """Getter for the original state of the sudoku board."""
        return self._original

    @property
    def solved(self) -> Optional[SudokuBoard]:
        """
        Getter for the solved version of the Sudoku game board.
        Will try to solve if not yet attempted.

        Returns
        -------
        Optional[SudokuBoard]
            A solved SudokuBoard, or None if no solution to the original puzzle exists.
        """
        # check if sudoku has already been solved
        if not self._solve_attempted:
            self.solve_original()

        return self._solved

    def show_board(self) -> None:
        """Print the current state of the Sudoku game board."""
        print(_board_string(self._board, "Current board"))

    def show_original(self) -> None:
        """Print the original state of the Sudoku game board."""
        print(_board_string(self._original, "Original board"))

    def show_solved(self) -> None:
        """Print the solved state of the Sudoku game board."""
        if self.solved is not None:
            print(_board_string(self.solved, "Solved"))
        else:
            print("No solution exists for this Sudoku.")

    def solve_original(self) -> None:
        """Try to solve the original sudoku puzzle."""
        self._solved = _recursive_solve(self._original)
        self._solve_attempted = True

    def reset_board(self) -> None:
        """Reset the sudoku to its original state."""
        self._board = deepcopy(self._original)

    def is_valid(self) -> bool:
        """Check if the current board is valid or not."""
        try:
            self._validate()
            print("Current board is valid.")
            return True
        except TypeError:
            print("Error: Current board is not valid.")
            return False

    def __repr__(self) -> str:
        """Default representation is the current state of the game board."""
        return _board_string(self._board)

    def _validate(self):
        """
        Check that the current board is a valid Sudoku puzzle.

        No return, will raise an exception on failed validation.
        """
        try:
            assert isinstance(self._board, list)
            assert len(self._board) == 9
            for row in self._board:
                assert isinstance(row, list)
                assert len(row) == 9
                for num in row:
                    assert isinstance(num, int)
                    assert 0 <= num
                    assert num <= 9
        except AssertionError as error:
            raise TypeError(
                "Sudoku is invalid, has incorrect structure or values."
            ) from error

        if _check_for_duplicates(self._board):
            raise TypeError("Sudoku is invalid, has duplicate values.")

    def save_as_image(self, location: str) -> None:
        """
        Saves the current board as an image file.

        Parameters
        ----------
        location : str
            File location for where the image should be saved.
        """
        raise NotImplementedError()
