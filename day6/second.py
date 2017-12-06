import sys


def redis(N, banks):
    i, n = max(enumerate(banks), key=lambda a: a[1])
    al = n // N
    new_b = []
    for j in range(N):
        new_b.append((banks[j] + al) if j != i else al)
    for j in range(i + 1, i + 1 + (n % N)):
        new_b[j % N] += 1
    return tuple(new_b)

def main():
    lines = []
    for line in sys.stdin.readlines():
        lines.append(line.strip())
    banks = tuple(int(x) for x in lines[0].split())
    N = len(banks)
    seen = set()
    count = 0
    while banks not in seen:
        count += 1
        seen.add(banks)
        #print(banks)
        banks = redis(N, banks)
    find_me = banks
    new_i = 1
    banks = redis(N, banks)
    while banks != find_me:
        new_i += 1
        banks = redis(N, banks)
    print(new_i)


if __name__ == '__main__':
    main()
