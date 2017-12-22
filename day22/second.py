import sys

DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

class State:
    WEAK  = 0
    INFEC = 1
    FLAG  = 2
    CLEAN = 3

INFEC_COUNT = 0

def vec_add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def tick(grid, pos, d):
    d = (d + grid[pos]) % 4
    grid[pos] = (grid[pos] + 1) % 4
    if grid[pos] == State.INFEC:
        global INFEC_COUNT
        INFEC_COUNT += 1
    pos = vec_add(pos, DIRS[d])
    return pos, d

class GridDict(dict):
    def __init__(self, start_grid):
        self.sgrid = start_grid

    def __missing__(self, item):
        x, y = item
        if 0 <= x < len(self.sgrid) and 0 <= y < len(self.sgrid[0]):
            return State.INFEC if self.sgrid[x][y] == '#' else State.CLEAN
        return State.CLEAN

def simulate(iters, grid, pos):
    d = 0
    for _ in range(iters):
        pos, d = tick(grid, pos, d)
    return pos

def main():
    sgrid = []
    for line in sys.stdin.readlines():
        line = line.strip()
        sgrid.append(list(line))
    gd = GridDict(sgrid)
    pos = (len(sgrid) // 2, len(sgrid[0]) // 2)

    simulate(10000000, gd, pos)
    print(INFEC_COUNT)

if __name__ == '__main__':
    main()
