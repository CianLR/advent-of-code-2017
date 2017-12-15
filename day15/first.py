import sys

ROUNDS = 40000000
MOD = 2147483647
A_FAC = 16807
B_FAC = 48271
MASK = (2 ** 16) - 1

def generator(val, factor):
    while True:
        val = (factor * val) % MOD
        yield val

def main():
    A = int(input().split()[-1])
    B = int(input().split()[-1])
    a_gen, b_gen = generator(A, A_FAC), generator(B, B_FAC)
    match = 0
    for _ in range(ROUNDS):
        a, b = next(a_gen), next(b_gen)
        if a & MASK == b & MASK:
            match += 1
    print(match)


if __name__ == '__main__':
    main()
