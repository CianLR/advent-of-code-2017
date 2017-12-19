import sys

def get_start(grid, H, W):
    for i in range(W):
        if grid[0][i] == '|':
            return (0, i)
    return None

def vec_add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def l(grid, p):
    return grid[p[0]][p[1]]

def in_bounds(p, H, W):
    return 0 <= p[0] < H and 0 <= p[1] < W

def follow_path(grid, start, H, W):
    out = ''
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    direc = 0
    cur = start
    steps = 0
    while cur:
        steps += 1
        v = l(grid, cur)
        if v.isalpha():
            out += v
        nex = vec_add(cur, dirs[direc])
        if in_bounds(nex, H, W) and l(grid, nex) != ' ':
            cur = nex
            continue
        # Nothing in front
        nex = vec_add(cur, dirs[(direc + 1) % 4])
        if in_bounds(nex, H, W) and l(grid, nex) != ' ':
            direc = (direc + 1) % 4
            cur = nex
            continue
        nex = vec_add(cur, dirs[(direc - 1) % 4])
        if in_bounds(nex, H, W) and l(grid, nex) != ' ':
            direc = (direc - 1) % 4
            cur = nex
            continue
        break
    return steps


def main():
    grid = []
    for line in sys.stdin.readlines():
        line = line.strip('\n')
        if line:
            grid.append(list(line))
    H = len(grid)
    W = len(grid[0])

    start = get_start(grid, H, W)
    print(follow_path(grid, start, H, W))



if __name__ == '__main__':
    main()
