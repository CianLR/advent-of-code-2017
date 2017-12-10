import sys

def rev_list(l, start, length):
    tmp = l[start:] + l[:start]
    tmp[:length] = reversed(tmp[:length])
    return tmp[-start:] + tmp[:-start]

LIST_SIZE = 256

def main():
    lengths = [int(x) for x in input().split(',')]
    knots = list(range(LIST_SIZE))
    skip_size = 0
    start_i = 0
    for l in lengths:
        knots = rev_list(knots, start_i, l)
        start_i = (start_i + l + skip_size) % len(knots)
        skip_size += 1
    print(knots[0] * knots[1])

if __name__ == '__main__':
    main()
