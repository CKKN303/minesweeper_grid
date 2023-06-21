# Minesweeper Grid

## Description
This simple Minesweeper grid converter is a Python project that implements the classic Minesweeper game functionality. Given a grid of '#' and '-', where each '#' represents a mine and each '-' represents a mine-free spot, the program calculates and replaces each dash '-' with a digit indicating the number of adjacent mines (horizontally, vertically, and diagonally).

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
To install and run the Minesweeper Grid project locally, follow these steps:

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/CKKN303/minesweeper_grid.git
   ```

2. Navigate to the project directory:
   ```shell
   cd minesweeper_grid
   ```
Remember to replace "your-username" with your own GitHub username if you want to clone the repository under your account.

Note: If you already have the repository cloned, make sure to fetch the latest changes from the remote repository using git pull before navigating to the project directory.

## Usage
Once you have installed the project, you can use it as follows:

1. Open the project in your preferred Python IDE or editor.

2. Modify the `grid` variable in the `main.py` file with your desired Minesweeper grid.

3. Run the `main.py` file.

4. The program will calculate the mine counts and display the resulting grid with the counts.

Here's an example usage:

```python
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

result = mine_count(grid)
for row in result:
    print(row)
```

This will display the resulting grid with the counts of adjacent mines.

## Credits
This Minesweeper Grid project is created by [Cecilie Kirkedal] as part of the course content for HyperionDev's Data Science Bootcamp.

If you have any questions or suggestions, feel free to [contact the author](mailto:kirkedalc@gmail.com).
```
