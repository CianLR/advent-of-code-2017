import sys

class Node:
    def __init__(self, name, weight, connects):
        self.name = name
        self.weight = weight
        self.overall_weight = None
        self.connects = connects


def set_weights(nodes, n):
    w = nodes[n].weight
    for ch in nodes[n].connects:
        w += set_weights(nodes, ch)
    nodes[n].overall_weight = w
    return w

def check_balance(nodes, n):
    ch_ws = [nodes[c].overall_weight for c in nodes[n].connects]
    a, b = min(ch_ws), max(ch_ws)
    if a == b:
        return None
    odd_index = -1
    good_index = -1
    if ch_ws.count(a) < ch_ws.count(b):
        odd_index = ch_ws.index(a)
        good_index = ch_ws.index(b)
    else:
        odd_index = ch_ws.index(b)
        good_index = ch_ws.index(a)

    new_w = check_balance(nodes, nodes[n].connects[odd_index])
    if new_w:
        return new_w
    diff = ch_ws[good_index] - ch_ws[odd_index]
    return nodes[nodes[n].connects[odd_index]].weight + diff

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

    set_weights(nodes, n)
    print(check_balance(nodes, n))


if __name__ == '__main__':
    main()
