from sys import stdin

def main():
    v = 0
    for l in stdin.readlines():
        w = l.strip().split()
        if len(set(w)) == len(w):
            v += 1
    print(v)


if __name__ == '__main__':
    main()

