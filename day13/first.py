import sys

def scanner_leaving(t, r):
    return (r - 1) - abs(-(r - 1) + (t % ((r - 1) * 2)))

def main():
    scanners = []
    for line in sys.stdin.readlines():
        depth, rnge = map(int, line.strip().split(': '))
        scanners.append((depth, rnge))

    sev = 0
    for d, r in scanners:
        if scanner_leaving(d, r) == 0:
            sev += d * r
    print(sev)


if __name__ == '__main__':
    main()
