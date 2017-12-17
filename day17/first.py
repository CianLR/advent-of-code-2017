import sys

def step_n(buf, cur, n):
    i = (cur + n) % len(buf)
    insert_point = (i + 1) % len(buf)
    buf.insert(insert_point, len(buf))
    return insert_point

def run_cycles(iterations, steps):
    buf = [0]
    i = 0
    for _ in range(iterations):
        i = step_n(buf, i, steps)
    return buf[(i + 1) % len(buf)]


def main():
    N = int(input())
    print(run_cycles(2017, N))

if __name__ == '__main__':
    main()
