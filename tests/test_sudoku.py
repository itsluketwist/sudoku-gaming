"""Tests for the `Sudoku` class."""

import pytest

from sudoku_gaming import Sudoku
from tests.utils import assert_complete_sudoku


@pytest.mark.parametrize(
    "input",
    [
        (
            [
                [3, 1, 0, 0, 6, 9, 0, 2, 4],
                [0, 0, 0, 7, 0, 0, 5, 0, 3],
                [5, 0, 0, 0, 4, 3, 0, 0, 8],
                [0, 0, 0, 0, 0, 7, 1, 0, 0],
                [0, 9, 0, 0, 5, 4, 3, 0, 0],
                [0, 0, 4, 0, 0, 1, 9, 8, 0],
                [0, 8, 0, 0, 0, 5, 0, 3, 1],
                [0, 3, 5, 8, 0, 0, 0, 6, 0],
                [4, 7, 2, 3, 1, 6, 8, 5, 9],
            ]
        ),
        (
            "310069024,000700503,500043008,"
            + "000007100,090054300,004001980,"
            + "080005031,035800060,472316859"
        ),
    ],
)
def test_sudoku_class(input):
    # init the sudoku
    sudoku = Sudoku(input)

    # check boards are set up correctly
    assert sudoku.original == [
        [3, 1, 0, 0, 6, 9, 0, 2, 4],
        [0, 0, 0, 7, 0, 0, 5, 0, 3],
        [5, 0, 0, 0, 4, 3, 0, 0, 8],
        [0, 0, 0, 0, 0, 7, 1, 0, 0],
        [0, 9, 0, 0, 5, 4, 3, 0, 0],
        [0, 0, 4, 0, 0, 1, 9, 8, 0],
        [0, 8, 0, 0, 0, 5, 0, 3, 1],
        [0, 3, 5, 8, 0, 0, 0, 6, 0],
        [4, 7, 2, 3, 1, 6, 8, 5, 9],
    ]
    assert sudoku.board == [
        [3, 1, 0, 0, 6, 9, 0, 2, 4],
        [0, 0, 0, 7, 0, 0, 5, 0, 3],
        [5, 0, 0, 0, 4, 3, 0, 0, 8],
        [0, 0, 0, 0, 0, 7, 1, 0, 0],
        [0, 9, 0, 0, 5, 4, 3, 0, 0],
        [0, 0, 4, 0, 0, 1, 9, 8, 0],
        [0, 8, 0, 0, 0, 5, 0, 3, 1],
        [0, 3, 5, 8, 0, 0, 0, 6, 0],
        [4, 7, 2, 3, 1, 6, 8, 5, 9],
    ]

    # set a value in the board
    sudoku.set(5, 3, 7)

    # check original has remained the same, and the current bopard has updated
    assert sudoku.original == [
        [3, 1, 0, 0, 6, 9, 0, 2, 4],
        [0, 0, 0, 7, 0, 0, 5, 0, 3],
        [5, 0, 0, 0, 4, 3, 0, 0, 8],
        [0, 0, 0, 0, 0, 7, 1, 0, 0],
        [0, 9, 0, 0, 5, 4, 3, 0, 0],
        [0, 0, 4, 0, 0, 1, 9, 8, 0],
        [0, 8, 0, 0, 0, 5, 0, 3, 1],
        [0, 3, 5, 8, 0, 0, 0, 6, 0],
        [4, 7, 2, 3, 1, 6, 8, 5, 9],
    ]
    assert sudoku.board == [
        [3, 1, 0, 0, 6, 9, 0, 2, 4],
        [0, 0, 0, 7, 0, 0, 5, 0, 3],
        [5, 0, 0, 0, 4, 3, 0, 0, 8],
        [0, 0, 0, 0, 0, 7, 1, 0, 0],
        [0, 9, 7, 0, 5, 4, 3, 0, 0],
        [0, 0, 4, 0, 0, 1, 9, 8, 0],
        [0, 8, 0, 0, 0, 5, 0, 3, 1],
        [0, 3, 5, 8, 0, 0, 0, 6, 0],
        [4, 7, 2, 3, 1, 6, 8, 5, 9],
    ]

    # check valid
    assert sudoku.is_valid() is True

    # set a value that will fail validation
    sudoku.set(3, 3, 7)

    # check invalid
    assert sudoku.is_valid() is False

    # try to solve the original board
    sudoku.solve_original()

    # check correctly solved
    assert_complete_sudoku(board=sudoku.solved)
