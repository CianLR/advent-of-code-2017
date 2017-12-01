
def main():
    l = [int(x) for x in input()]
    s = 0
    h = len(l) // 2
    for i in range(len(l)):
        if l[i] == l[(i + h) % len(l)]:
            s += l[i]
    print(s)

if __name__ == '__main__':
    main()

