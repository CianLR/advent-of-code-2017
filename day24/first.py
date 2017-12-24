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

MEMO = {}
def dfs(comps, ports, seen, cur):
    if (seen, cur) in MEMO:
        return MEMO[(seen, cur)]
    mx = 0
    for i in ports[cur]:
        if i in seen:
            continue
        mx = max(mx,
                 comps[i].strength + dfs(comps,
                                         ports,
                                         seen | {i},
                                         comps[i].other(cur)))
    MEMO[(seen, cur)] = mx
    return mx

def main():
    components = []
    ports = defaultdict(list)
    for i, line in enumerate(sys.stdin.readlines()):
        a, b = map(int, line.split('/'))
        components.append(Component(a, b))
        ports[a].append(i)
        ports[b].append(i)
    
    print(dfs(components, ports, frozenset(), 0))



if __name__ == '__main__':
    main()
