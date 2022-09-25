# **sudoku-gaming**

A sudoku gameplay client, including:
- a sudoku generator with difficulty options,
- and an efficient sudoku solver using a depth-first backtracking algorithm.

## *usage*

There are multiple ways to interact with the repository:
- `Sudoku` class is provided, that allows you to initialise a sudoku puzzle from a 9x9 array
  or a comma-string, and then print or interact with it
- `generate` method, that creates a `Sudoku` of a certain difficulty
- `solve` method, that will solve a `Sudoku`, or determine a solution does not exist.

*Note: zeroes are used to denote 'empty' cells in the sudoku puzzle throughout.*

```python
from sudoku_gaming import Sudoku, generate, solve


# sudoku from list
sudoku_1 = Sudoku([
    [7, 9, 0, 1, 2, 0, 8, 6, 0],
    [0, 0, 2, 9, 8, 0, 5, 0, 0],
    [0, 0, 8, 0, 3, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 3, 5, 6],
    [0, 5, 3, 0, 0, 8, 2, 0, 9],
    [0, 0, 9, 0, 0, 3, 0, 8, 1],
    [9, 8, 0, 5, 0, 0, 0, 0, 0],
    [0, 2, 5, 3, 9, 1, 0, 0, 8],
    [1, 3, 7, 8, 6, 2, 0, 0, 0],
])
sudoku_1.print_board()


# sudoku from string
sudoku_2 = Sudoku(
    "310069024,000700503,500043008,000007100,090054300,004001980,080005031,035800060,472316859"
)
sudoku_2.print_board()


# create, display and solve an easy sudoku
easy_sudoku = generate(difficulty=3)
easy_sudoku.print_board()

easy_solved = solve(easy_sudoku)
easy_solved.print_board()


# create, display and solve an hard sudoku
hard_sudoku = generate(difficulty=8)
hard_sudoku.print_board()

hard_solved = solve(hard_sudoku)
hard_solved.print_board()
```


## *development*

Install and use pre-commit to ensure code is in a good state:

```shell
python -m venv venv

. venv/bin/activate

pip install pre-commit

pre-commit install

pre-commit run --all-files
```


## *to-do*

- Complete `play(...)` method.
- Complete `Sudoku.save_as_image(...)` method.
- Turn into a package.
- Add some basic testing.
