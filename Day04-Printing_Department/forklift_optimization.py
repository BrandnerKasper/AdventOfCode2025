grid_map = {
    "." : 0,
    "@" : 1,
    "x" : 2}
def turn_str_into_grid(grid: str) -> list[list[int]]:
    g = []
    for l in grid.splitlines():
        line = []
        for c in l:
            line.append(grid_map[c])
        g.append(line)
    return g


def mark(grid: list[list[int]]) -> list[list[int]]:
    copy = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == 1 and check_adjacent_positions(grid, y, x):
                copy[y][x] = 2
            else:
                copy[y][x] = grid[y][x]
    return copy


def check_adjacent_positions(grid: list[list[int]], y: int, x: int) -> bool:
    c = 0
    m_len = len(grid)-1
    if y > 0 and x > 0: # top left
        c += grid[y-1][x-1] == 1
    if y > 0: # top
        c += grid[y-1][x] == 1
    if y > 0 and x < m_len: # top right
        c+= grid[y-1][x+1] == 1
    if x > 0: # left
        c+= grid[y][x-1] == 1
    if x < m_len: # right
        c+= grid[y][x+1] == 1
    if y < m_len and x > 0: # bottom left
        c+= grid[y+1][x-1] == 1
    if y < m_len: # bottom
        c += grid[y+1][x] == 1
    if y < m_len and x < m_len: # bottom right
        c += grid[y+1][x+1] == 1
    return c < 4


str_map = {
    0 : ".",
    1 : "@",
    2 : "x"
}
def turn_grid_into_str(grid: list[list[int]]) -> str:
    s = ""
    for l in grid:
        for n in l:
            s += str_map[n]
        s += "\n"
    s = s[:-1]
    return s


def count_x(grid: str) -> int:
    count = 0
    for l in grid.splitlines():
        for c in l:
            if c == "x":
                count += 1
    return count


def fork_optimization(grid: str) -> int:
    grid = turn_str_into_grid(grid)
    grid = mark(grid)
    grid = turn_grid_into_str(grid)
    count = count_x(grid)
    return count


def fork_clean_up(grid: str) -> int:
    total = 0
    removed = True
    while removed:
        grid = turn_str_into_grid(grid)
        grid = mark(grid)
        grid = turn_grid_into_str(grid)
        count = count_x(grid)
        total += count
        if count == 0:
            removed = False
        print(f"Removed {count} roll(s) of paper.")
        print(grid)
        grid = grid.replace("x", ".")
    return total


def parse_forklift_map(file: str) -> str:
    s = ""
    with open(file, "r") as f:
        for l in f:
            s += l
    return s


def main() -> None:
    file = "forklift.txt"
    m = parse_forklift_map(file)
    print(f"Number of optimizations: {fork_optimization(m)}")
    print(f"Total number of optimization with cleanup in mind: {fork_clean_up(m)}")


if __name__ == "__main__":
    main()
