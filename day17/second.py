
def last_land_zero(iters, step):
    i = 0
    last_zero = None
    for buf_len in range(1, 1 + iters):
        i = ((i + step) % buf_len) + 1
        if i == 1:
            last_zero = buf_len
    return last_zero

def main():
    step = int(input())
    cycles = 50000000
    print(last_land_zero(cycles, step))


if __name__ == '__main__':
    main()

