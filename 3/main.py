import math


def traverse(grid, x_diff, y_diff):
    c, x, y = 0, 0, 0
    y_end = len(grid)
    x_end = len(grid[0])

    while True:
        if grid[y][x] == '#':
            c += 1

        x = (x + x_diff) % x_end
        y += y_diff

        if y >= y_end:
            break

    return c


grid = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#',
]


with open('input.txt') as file:
    grid = file.readlines()
    grid = [row.replace('\n', '') for row in grid]

# print(traverse(grid))

res = [traverse(grid, x, y) for x, y in [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)]]

print(math.prod(res))
