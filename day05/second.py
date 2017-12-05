import sys



def main():
    jumps = []
    for line in sys.stdin.readlines():
        line = line.strip()
        jumps.append(int(line))
    i = 0
    t = 0
    while 0 <= i < len(jumps):
        n = i
        i += jumps[i]
        if jumps[n] >= 3:
            jumps[n] -= 1
        else:
            jumps[n] += 1
        t += 1
    print(t)


if __name__ == '__main__':
    main()
