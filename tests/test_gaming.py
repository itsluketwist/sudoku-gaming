"""Tests for the gaming funtions `generate` and `solve`."""

import pytest

from sudoku_gaming import generate, solve
from tests.utils import assert_complete_sudoku, count_blanks


@pytest.mark.parametrize(
    "difficulty, expected_blanks",
    [
        (0, 9),
        (1, 9),
        (2, 17),
        (3, 25),
        (4, 33),
        (5, 41),
        (6, 49),
        (7, 57),
        (8, 65),
        (9, 72),
        (10, 72),
    ],
)
def test_gaming_funcs(difficulty, expected_blanks):
    # create a new puzzle
    sudoku = generate(difficulty=difficulty)

    # check puzzle has the correct number of blank spaces
    assert count_blanks(board=sudoku.board) == expected_blanks

    # try to solve
    solve(sudoku=sudoku)

    # check correctly solved
    assert_complete_sudoku(board=sudoku.solved)


def test_gaming_solve_from_string():
    sudoku_string = (
        "310069024,000700503,500043008,"
        "000007100,090054300,004001980,"
        "080005031,035800060,472316859"
    )

    sudoku = solve(sudoku=sudoku_string)

    # check correctly solved
    assert_complete_sudoku(board=sudoku.solved)
