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

def run_cycle(grid, instrs):
    ops = {'s': spin, 'x': exchange, 'p': partner}
    for line in instrs:
        op, args = line[0], line[1:]
        grid = ops[op](grid, *args.split('/'))
    return grid

def main():
    CYCLES = 1000000000
    grid = [chr(c) for c in range(ord('a'), ord('q'))]
    instrs = sys.stdin.read().strip().split(',')
    seen_states = set()
    states = []
    for _ in range(CYCLES):
        grid = run_cycle(grid, instrs)
        t_grid = tuple(grid)
        if t_grid in seen_states:
            break
        seen_states.add(t_grid)
        states.append(t_grid)

    print(''.join(states[(CYCLES - 1) % len(states)]))

if __name__ == '__main__':
    main()
