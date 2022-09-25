from copy import deepcopy
from typing import List, Union

SudokuBoard = List[List[int]]


class Sudoku:
    """
    An object representing a sudoku puzzle, containing a game board and logic
    to update it's cells and display it.
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

    def get(self, row: int, col: int) -> int:
        """Return the value of a cell from the sudoku board."""
        return self._board[row][col]

    def set(self, row: int, col: int, value: int) -> None:
        """Update the value of a cell in the sudoku board."""
        self._board[row][col] = value

    @property
    def board(self) -> SudokuBoard:
        """Getter for the current state of the sudoku board."""
        return self._board

    def print_board(self) -> None:
        """Print the current state of the Sudoku game board."""
        print(self._board_string(self._board))

    @property
    def original(self) -> SudokuBoard:
        """Getter for the original state of the sudoku board."""
        return self._original

    def print_original(self) -> None:
        """Print the original state of the Sudoku game board."""
        print(self._board_string(self._original))

    def _board_string(self, board: SudokuBoard) -> str:
        """Get a printable string representation of a SudokuBoard."""
        return (
            "\nSudoku:\n"
            + "\n".join([" ".join([str(n) for n in row]) for row in board])
            + "\n"
        )

    def __repr__(self) -> str:
        """Default representation is the current state of the game board."""
        return self._board_string(self._board)

    def _validate(self):
        """Check that a valid Sudoku was created from the provided input array or string."""
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

        if self._check_for_duplicates():
            raise TypeError("Sudoku is invalid, has duplicate values.")

    def _check_for_duplicates(self) -> bool:
        """Check for duplicate numbers in each row, column and grid of the sudoku."""
        # first check the rows and columns for their non-zero entries
        for index in range(9):
            row_nums = [self.get(index, y) for y in range(9) if self.get(index, y) != 0]
            col_nums = [self.get(x, index) for x in range(9) if self.get(x, index) != 0]

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
                        num = self.get(x, y)
                        if num != 0 and num in grid_nums:
                            return True
                        else:
                            grid_nums.add(num)

        # no duplicates found
        return False

    def save_as_image(self, location: str) -> None:
        raise NotImplementedError()
