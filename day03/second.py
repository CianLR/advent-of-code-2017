from collections import defaultdict
import numpy as np

UP    = np.array([0, 1])
LEFT  = np.array([-1, 0])
DOWN  = np.array([0, -1])
RIGHT = np.array([1, 0])

class MyDD(defaultdict):
    def __getitem__(self, key):
        if 'tostring' in dir(key):
            key = key.tostring()
        return defaultdict.__getitem__(self, key)
    
    def __setitem__(self, key, i):
        if 'tostring' in dir(key):
            key = key.tostring()
        return defaultdict.__setitem__(self, key, i)

grid = MyDD(int)
cent = np.array([50, 50])
grid[cent] = 1

def sum_nbrs(p):
    s = 0
    for d in [UP, LEFT, DOWN, RIGHT,
              UP + LEFT, UP + RIGHT,
              DOWN + LEFT, DOWN + RIGHT]:
        s += grid[p + d]
    return s

def do_move_n(p, move, times, N):
    for _ in range(times):
        p += move
        n = sum_nbrs(p)
        if n > N:
            return n
        grid[p] = n
    return None

def walk_spiral(p, level, N):
    K = 2 * level
    n = do_move_n(p, RIGHT, 1, N)
    if n: return n
    n = do_move_n(p, UP, K - 1, N)
    if n: return n
    n = do_move_n(p, LEFT, K, N)
    if n: return n
    n = do_move_n(p, DOWN, K, N)
    if n: return n
    n = do_move_n(p, RIGHT, K, N)
    if n: return n 
    return None

def main():
    N = int(input())
    if N == 1:
        print("No")
        return
    p = np.array([50, 50])
    level = 1
    while True:
        n = walk_spiral(p, level, N)
        if n:
            print(n)
            break
        level += 1
    print(p)


if __name__ == '__main__':
    main()

