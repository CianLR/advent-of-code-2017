import sys

DIRS = {
    'n': (0, 1),
    'ne': (0.5, 0.5),
    'se': (0.5, -0.5),
    's': (0, -1),
    'sw': (-0.5, -0.5),
    'nw': (-0.5, 0.5),
}

def vec_add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def walk_path(point, path):
    for p in path:
        point = vec_add(point, DIRS[p])
    return point

def hex_dist(point):
    return int(abs(point[0]) + abs(point[1]))


def path_dist(path):
    point = walk_path((0, 0), path)
    return hex_dist(point)

def test():
    TESTS = [
        ('ne,ne,ne', 3),
        ('ne,ne,sw,sw', 0),
        ('ne,ne,s,s', 2),
        ('se,sw,se,sw,sw', 3),
    ]
    for i, o in TESTS:
        print(i, o, path_dist(i.split(',')))

def main():
    path = input().split(',')
    print(path_dist(path))    

if __name__ == '__main__':
    main()
