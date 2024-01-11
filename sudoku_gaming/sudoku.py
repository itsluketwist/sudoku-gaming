from copy import deepcopy
from datetime import datetime

from sudoku_gaming.types import SudokuBoard
from sudoku_gaming.utils import (
    _board_string,
    _check_for_duplicates,
    _get_table_fill_color_matrix,
    _recursive_solve,
)


class Sudoku:
    """
    An object representing a sudoku puzzle, containing a game board and logic
    to update the board state and display it.
    """

    def __init__(self, board: SudokuBoard | str | None = None):
        """
        Parameters
        ----------
        board: SudokuBoard | str | None = None
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
        self._solved: SudokuBoard | None = None
        self._solve_attempted = False

    def get(self, row: int, col: int) -> int | None:
        """
        Return the value of a cell from the sudoku board.

        Parameters
        ----------
        row: int
            Must be a value between 1 and 9 inclusive.
        col: int
            Must be a value between 1 and 9 inclusive.

        Returns
        -------
        int | None
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
        row: int
            Must be a value between 1 and 9 inclusive.
        col: int
            Must be a value between 1 and 9 inclusive.
        value: int
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
    def solved(self) -> SudokuBoard | None:
        """
        Getter for the solved version of the Sudoku game board.
        Will try to solve if not yet attempted.

        Returns
        -------
        SudokuBoard | None
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

    def save_as_image(self, location: str = "./", name: str | None = None) -> None:
        """
        Saves the current board as a png image file.

        Parameters
        ----------
        location: str = "./"
            File location for where the image should be saved.
        name: str | None = None
            Name of the file to save, excluding the file extension.
            If None, will default to `sudoku_{current_datetime}`.
        """
        try:
            import plotly.graph_objects as go

            # default the file name
            if name is None:
                name = f"sudoku_{datetime.now().isoformat()}"

            # build list of column data
            table_data = []
            for col in range(9):
                _next_col = []
                for row in range(9):
                    if self._board[row][col] == 0:
                        _next_col.append("")
                    else:
                        _next_col.append(f"{self._board[row][col]}")
                table_data.append(_next_col)

            fig = go.Figure(
                data=[
                    go.Table(
                        header=dict(
                            fill_color="rgba(0,0,0,0)",
                        ),
                        cells=dict(
                            values=table_data,
                            height=30,
                            align="center",
                            fill_color=_get_table_fill_color_matrix(),
                        ),
                        columnwidth=30,
                    ),
                ],
                layout=go.Layout(
                    dict(
                        width=500,
                        height=500,
                    )
                ),
            )
            fig.write_image(f"{location}{name}.png")

        except ImportError:
            print(
                "InstallError: You must install with the 'img' extra in order to save images."
            )
