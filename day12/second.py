import sys
from collections import defaultdict


def bfs(nodes, start):
    q = [start]
    seen = set()
    while q:
        u, *q = q
        if u in seen:
            continue
        seen.add(u)
        for v in nodes[u]:
            if v not in seen:
                q.append(v)
    return seen

def main():
    nodes = defaultdict(list)
    for line in sys.stdin.readlines():
        line = line.strip()
        start, _, *oth = line.split()
        for v in oth:
            nodes[int(start)].append(int(v.strip(',')))

    groups = 0
    seen = set()
    for n in nodes:
        if n in seen:
            continue
        groups += 1
        seen.update(bfs(nodes, n))
    print(groups)

if __name__ == '__main__':
    main()
