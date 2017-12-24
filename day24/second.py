import sys
from collections import defaultdict

class Component:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.strength = a + b
    
    def other(self, v):
        if v == self.a:
            return self.b
        return self.a

def dfs(comps, ports, seen, cur, l):
    mx = (l, 0)
    for i in ports[cur]:
        if i in seen:
            continue
        best = dfs(comps, ports, seen | {i}, comps[i].other(cur), l + 1)
        mx = max(mx, (best[0], best[1] + comps[i].strength))
    return mx

def main():
    components = []
    ports = defaultdict(list)
    for i, line in enumerate(sys.stdin.readlines()):
        a, b = map(int, line.split('/'))
        components.append(Component(a, b))
        ports[a].append(i)
        ports[b].append(i)
    
    print(dfs(components, ports, set(), 0, 0))



if __name__ == '__main__':
    main()
