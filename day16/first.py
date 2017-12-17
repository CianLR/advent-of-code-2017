import sys

def spin(grid, n):
    n = int(n)
    return grid[-n:] + grid[:-n]

def exchange(grid, a, b):
    a, b = int(a), int(b)
    grid[a], grid[b] = grid[b], grid[a]
    return grid

def partner(grid, a, b):
    ai = grid.index(a)
    bi = grid.index(b)
    return exchange(grid, ai, bi)

def main():
    grid = [chr(c) for c in range(ord('a'), ord('q'))]
    ops = {'s': spin, 'x': exchange, 'p': partner}
    for line in sys.stdin.read().split(','):
        op, args = line[0], line[1:]
        grid = ops[op](grid, *args.split('/'))
    print(''.join(grid))

if __name__ == '__main__':
    main()
