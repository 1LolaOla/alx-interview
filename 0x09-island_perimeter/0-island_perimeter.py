#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list[list[int]]): The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    if not grid:
        return perimeter

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 to perimeter

                # Check adjacent cells (up, down, left, right)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1  # Subtract for shared edge
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1  # Subtract for shared edge
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1  # Subtract for shared edge
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1  # Subtract for shared edge

    return perimeter

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]

    print(island_perimeter(grid))  # Output: 16

