import sys

def scanner_leaving(t, r):
    return (r - 1) - abs(-(r - 1) + (t % ((r - 1) * 2)))

def main():
    scanners = []
    for line in sys.stdin.readlines():
        depth, rnge = map(int, line.strip().split(': '))
        scanners.append((depth, rnge))

    delay = -1
    while True:
        delay += 1
        for d, r in scanners:
            if scanner_leaving(d + delay, r) == 0:
                break
        else:
            break
    print(delay)


if __name__ == '__main__':
    main()
