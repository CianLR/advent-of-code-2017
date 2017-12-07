import sys

class Node:
    def __init__(self, name, weight, connects):
        self.name = name
        self.weight = weight
        self.connects = connects


def main():
    parents = {}
    nodes = {}
    for line in sys.stdin.readlines():
        line = line.strip()
        name, weight, *connects = line.split(' ', 2)
        below = []
        if connects:
            below = connects[0][3:].split(', ')
            for n in below:
                parents[n] = name
        nodes[name] = Node(name, int(weight[1:-1]), below)

    n = next(iter(nodes))
    while n in parents:
        n = parents[n]
    print(n)


if __name__ == '__main__':
    main()
