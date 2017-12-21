import sys
from operator import add
from functools import reduce

def slash_to_tup(sl):
    return tuple(tuple(s) for s in sl.split('/'))

def flip(sq):
    return tuple(l[::-1] for l in sq)

def rotate(sq):
    return tuple(zip(*sq))[::-1]

def split_grid(grid, n):
    out_grids = []
    for i in range(0, len(grid), n):
        for j in range(0, len(grid), n):
            g = []
            for k in range(i, i + n):
                line = []
                for l in range(j, j + n):
                    line.append(grid[k][l])
                g.append(tuple(line))
            out_grids.append(tuple(g))
    return out_grids

def join_grid(grids):
    # (((1, 2), (3, 4)), (1, 2...
    # ((1, 2, 1, 2), (3, 4, 3, 4), (1, 2...
    out_grid = []
    per_row = int(len(grids) ** 0.5)
    for i in range(0, len(grids), per_row):
        out_grid.extend([reduce(add, r) for r in zip(*grids[i:i + per_row])])
    return tuple(out_grid)
        

def apply_transition(trs, grid):
    gs = split_grid(grid, 3) if len(grid) % 2 else split_grid(grid, 2)
    replaced_g = []
    for g in gs:
        replaced_g.append(trs[g])
    return join_grid(replaced_g)

def on_pixels(grid):
    return sum(l.count('#') for l in grid)

def main():
    transitions = {}
    for line in sys.stdin.readlines():
        line = line.strip()
        pat, out = map(slash_to_tup, line.split(' => '))
        for _ in range(4):
            pat = rotate(pat)
            transitions[pat] = out
            transitions[flip(pat)] = out

    grid = (('.', '#', '.'), ('.', '.', '#'), ('#', '#', '#'))
    for _ in range(18):
        grid = apply_transition(transitions, grid)
    print(on_pixels(grid))

if __name__ == '__main__':
    main()
