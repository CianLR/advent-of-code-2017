
def main():
    l = [int(x) for x in input()]
    s = 0
    for i in range(len(l)):
        if l[i] == l[(i + 1) % len(l)]:
            s += l[i]
    print(s)

if __name__ == '__main__':
    main()

