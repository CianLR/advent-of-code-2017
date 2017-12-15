import sys

ROUNDS = 5000000
MOD = 2147483647
A_FAC = 16807
B_FAC = 48271
A_MUL = 4
B_MUL = 8
MASK = (2 ** 16) - 1

def generator(val, factor, mul):
    while True:
        val = (factor * val) % MOD
        if val % mul == 0:
            yield val

def main():
    A = int(input().split()[-1])
    B = int(input().split()[-1])
    a_gen, b_gen = generator(A, A_FAC, A_MUL), generator(B, B_FAC, B_MUL)
    match = 0
    for _ in range(ROUNDS):
        a, b = next(a_gen), next(b_gen)
        if a & MASK == b & MASK:
            match += 1
    print(match)


if __name__ == '__main__':
    main()
