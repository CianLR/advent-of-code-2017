import numpy as np

UP    = np.array([0, 1])
LEFT  = np.array([-1, 0])
DOWN  = np.array([0, -1])
RIGHT = np.array([1, 0])

def get_spiral_level(n):
    l = 1
    n -= 2
    spiral_size = 8
    while n - spiral_size >= 0:
        n -= spiral_size
        spiral_size += 8
        l += 1
    return l, n

def walk_spiral(p, level, index):
    K = 2 * level
    i = 0
    for _ in range(K - 1):
        if i == index:
            return p
        p += UP
        i += 1
    for _ in range(K):
        if i == index:
            return p
        p += LEFT
        i += 1
    for _ in range(K):
        if i == index:
            return p
        p += DOWN
        i += 1
    for _ in range(K):
        if i == index:
            return p
        p += RIGHT
        i += 1
    return p

def dist(p):
    return abs(p[0]) + abs(p[1])

def main():
    N = int(input())
    if N == 1:
        print("No")
        return
    level, index = get_spiral_level(N)
    p = np.array([1, 0]) + (np.array([1, -1]) * (level - 1))
    p = walk_spiral(p, level, index)
    print(p)
    print(dist(p))


if __name__ == '__main__':
    main()

