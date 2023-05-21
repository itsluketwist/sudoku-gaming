# **sudoku-gaming**

A simple sudoku gameplay client, including:
- a sudoku generator with difficulty options,
- and an efficient sudoku solver using a depth-first backtracking algorithm.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## *installation*

Install directly from GitHub, using pip:

```shell
pip install git+https://github.com/itsluketwist/sudoku-gaming
```

Use the `img` extra when installing to be able to save sudokus as images:

```shell
pip install git+https://github.com/itsluketwist/sudoku-gaming#egg=sudoku_gaming[img]
```


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
sudoku_1.show_board()
sudoku_1.show_solved()

# sudoku from string
sudoku_2 = Sudoku(
  "310069024,000700503,500043008,000007100,090054300,004001980,080005031,035800060,472316859"
)
sudoku_2.show_board()
sudoku_2.show_solved()

# create, display and solve an easy sudoku
easy_sudoku = generate(difficulty=3)
easy_sudoku.show_board()
easy_sudoku.show_solved()

# create, display and solve a hard sudoku
hard_sudoku = generate(difficulty=8)
hard_sudoku.show_board()
hard_sudoku.show_solved()
```


## *development*

Clone the repository code:

```shell
git clone https://github.com/itsluketwist/sudoku-gaming.git
```

Once cloned, install the package locally in a virtual environment:

```shell
python -m venv venv

. venv/bin/activate

pip install -e ".[dev,img]"
```

Install and use pre-commit to ensure code is in a good state:

```shell
pre-commit install

pre-commit run --all-files
```


## *testing*

Run the test suite using:

```shell
pytest .
```


## *inspiration*

I created the sudoku solver code as part of a project during my masters, and thought it would be fun to try
and expand the functionality, whilst getting practice in creating python packages.
