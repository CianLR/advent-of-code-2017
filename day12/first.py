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
    return len(seen)

def main():
    nodes = defaultdict(list)
    for line in sys.stdin.readlines():
        line = line.strip()
        start, _, *oth = line.split()
        for v in oth:
            nodes[int(start)].append(int(v.strip(',')))
    print(bfs(nodes, 0))

if __name__ == '__main__':
    main()
