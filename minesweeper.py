'''Task:
Create a function that takes a grid of # and -, where each hash (#) represents a
mine and each dash (-) represents a mine-free spot.
Return a grid, where each dash is replaced by a digit, indicating the number of
mines immediately adjacent to the spot i.e. (horizontally, vertically, and
diagonally).

Method:
- Create a function which calculates adjecent mines in a grid (2D list where each nested list is of equal length). 
    Declare row/col variables using len() to allow for dynamic grid size
    Declare variable containing relative positions of adjecent tiles
    Create variable to store result of mine count/new grid
    Use nested for loops to iterate over 2D list
        if item = #, leave as is
        else item = -, count number of mines in adjecent tiles
            use if statement to check for boundaries
    return new grid with mines counted
- Display result of function iterating over test grid with for loop using .join()
'''

# Minesweeper function which iterates over a 2D list, calculating how many instances of "#" are in a position adjacent to a "-"
def mine_count(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Variable containing adjacent tile positions relative to each tile
    adjacent_tiles = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    
    # Empty grid to store the result of mine count
    new_grid = [['' for _ in range(cols)] for _ in range(rows)]
    
    # Mine count. Iterates over the grid, checking each item for adjacent mines.
    for row in range(rows):
        for col in range(cols):
            # If tile is a mine, leaves it as is
            if grid[row][col] == "#":
                new_grid[row][col] = "#"
            # If tile is not a mine, checks adjacent tiles for presence of mines, adjusts the mine count
            else:
                count = 0
                for tile in adjacent_tiles:
                    tile_row = row + tile[0]
                    tile_col = col + tile[1]

                    # Checks for boundaries
                    if 0 <= tile_row < rows and 0 <= tile_col < cols:
                        if grid[tile_row][tile_col] == "#":
                            count += 1
                
                # Converts mine count to string
                new_grid[row][col] = str(count)

    return new_grid

# Test grids
grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]

grid_2 = [["#", "-", "-", "#", "-", "#"],
          ["#", "#", "-", "-", "-", "#"],
          ["-", "-", "-", "-", "#", "-"],
          ["-", "#", "#", "#", "-", "#"],
          ["-", "-", "-", "-", "-", "-"]]

# Prints output of mine count in a readable grid format
result = mine_count(grid)
for row in result:
    print(row)