def import_grid(filename: str) -> tuple:
    grid: list = []
    grid_file = open(filename, 'r')
    for line in grid_file:
        row: list = line.split()
        for item_index, item in enumerate(row):
            row[item_index]: int = int(item)
        grid.append(tuple(row))
    grid_file.close()
    return tuple(grid)


def find_verticals_product(grid: tuple, height: int, width: int, adjacent_length: int) -> int:
    greatest_product: int = 0
    for y_start_coordinate in range(0, height - adjacent_length + 1):
        for x_coordinate in range(0, width):
            adjacent_product: int = grid[y_start_coordinate][x_coordinate]
            for y_coordinate in range(y_start_coordinate+1, y_start_coordinate + adjacent_length):
                adjacent_product *= grid[y_coordinate][x_coordinate]
            if adjacent_product > greatest_product:
                greatest_product: int = adjacent_product
    return greatest_product


def find_horizontals_product(grid: tuple, height: int, width: int, adjacent_length: int) -> int:
    greatest_product: int = 0
    for x_start_coordinate in range(0, width - adjacent_length + 1):
        for y_coordinate in range(0, height):
            adjacent_product: int = grid[y_coordinate][x_start_coordinate]
            for x_coordinate in range(x_start_coordinate+1, x_start_coordinate + adjacent_length):
                adjacent_product *= grid[y_coordinate][x_coordinate]
            if adjacent_product > greatest_product:
                greatest_product: int = adjacent_product
    return greatest_product


def find_downward_diagonals_product(grid: tuple, height: int, width: int, adjacent_length: int) -> int:
    greatest_product: int = 0
    for x_start_coordinate in range(0, width - adjacent_length + 1):
        for y_start_coordinate in range(0, height - adjacent_length + 1):
            adjacent_product: int = grid[y_start_coordinate][x_start_coordinate]
            for start_offset in range(1, adjacent_length):
                adjacent_product *= grid[y_start_coordinate + start_offset][x_start_coordinate + start_offset]
            if adjacent_product > greatest_product:
                greatest_product: int = adjacent_product
    return greatest_product


def find_upward_diagonals_product(grid: tuple, height: int, width: int, adjacent_length: int) -> int:
    greatest_product: int = 0
    for x_start_coordinate in range(0, width - adjacent_length + 1):
        for y_start_coordinate in range(adjacent_length - 1, height):
            adjacent_product: int = grid[y_start_coordinate][x_start_coordinate]
            for start_offset in range(1, adjacent_length):
                adjacent_product *= grid[y_start_coordinate - start_offset][x_start_coordinate + start_offset]
            if adjacent_product > greatest_product:
                greatest_product: int = adjacent_product
    return greatest_product


def main(grid_filename: str = 'grid.txt', adjacent_length: int = 1):
    grid: tuple = import_grid(grid_filename)
    height: int = len(grid)
    width: int = len(grid[0])
    verticals: int = find_verticals_product(grid, height, width, adjacent_length)
    horizontals: int = find_horizontals_product(grid, height, width, adjacent_length)
    downward_diagonals: int = find_downward_diagonals_product(grid, height, width, adjacent_length)
    upward_diagonals: int = find_upward_diagonals_product(grid, height, width, adjacent_length)
    print(max(verticals, horizontals, downward_diagonals, upward_diagonals))


main(grid_filename='11-largest-product-in-a-grid.txt', adjacent_length=4)
