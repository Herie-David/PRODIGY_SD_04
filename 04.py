def is_valid(grid, row, col, num):
  # Checks if placing 'num' at (row, col) is valid according to Sudoku rules

  # Check row for duplicates
  for i in range(9):
    if grid[row][i] == num and col != i:
      return False

  # Check column for duplicates
  for i in range(9):
    if grid[i][col] == num and row != i:
      return False

  # Check subgrid for duplicates
  start_row = row - row % 3
  start_col = col - col % 3
  for i in range(3):
    for j in range(3):
      if grid[start_row + i][start_col + j] == num and (row, col) != (start_row + i, start_col + j):
        return False

  return True

def solve_sudoku(grid):
  # Solves the Sudoku puzzle using backtracking
  for row in range(9):
    for col in range(9):
      if grid[row][col] == 0:
        for num in range(1, 10):
          if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
              return True
            grid[row][col] = 0  # Backtrack if solution not found yet
        return False  # No valid number found for this cell, backtrack
  return True  # Puzzle solved successfully

def print_grid(grid):
  # Prints the Sudoku grid in a formatted way
  for i in range(9):
    for j in range(9):
      print(grid[i][j], end=" ")
      if (j + 1) % 3 == 0 and j != 8:
        print("|", end=" ")
    print()
    if (i + 1) % 3 == 0 and i != 8:
      print("-" * 27)

def main():
  # Prompts user for input and calls functions to solve and print
  grid = []
  print("Enter the Sudoku puzzle (0 for empty cells):")
  for i in range(9):
    row = [int(x) for x in input().split()]
    grid.append(row)

  if solve_sudoku(grid):
    print("\nSolved Sudoku:")
    print_grid(grid)
  else:
    print("No solution found for the given Sudoku puzzle.")

if __name__ == "__main__":
  main()