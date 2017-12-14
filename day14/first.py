import sys

LIST_SIZE = 256
SEED_LENS = [17, 31, 73, 47, 23]

def rev_list(l, start, length):
    tmp = l[start:] + l[:start]
    tmp[:length] = reversed(tmp[:length])
    return tmp[-start:] + tmp[:-start]

def hash_round(knots, lengths, skip_size=0, start_i=0):
    for l in lengths:
        knots = rev_list(knots, start_i, l)
        start_i = (start_i + l + skip_size) % len(knots)
        skip_size += 1
    return knots, skip_size, start_i

def do_rounds(knots, lengths, rounds=64):
    start = 0
    skip = 0
    for _ in range(rounds):
        knots, start, skip = hash_round(knots, lengths, start, skip)
    return knots

def make_dense_hash(knots):
    dense = [0] * (LIST_SIZE // 16)
    for i in range(LIST_SIZE // 16):
        for c in knots[i*16:(i + 1)*16]:
            dense[i] ^= c
    return dense

def knot_hash(key):
    lengths = [ord(c) for c in key] + SEED_LENS
    knots = do_rounds(list(range(LIST_SIZE)), lengths)
    return make_dense_hash(knots)

def knot_to_bin(dense):
    b = ''
    for c in dense:
        b += bin(c)[2:].zfill(8)
    return b

def make_grid(key):
    grid = []
    for i in range(128):
        kh = knot_hash("{}-{}".format(key, i))
        grid.append(knot_to_bin(kh))
        assert len(grid[-1]) == 128
    return grid

def get_used(key):
    grid = make_grid(key)
    used = 0
    for row in grid:
        used += row.count('1')
    return used

def main():
    key = input()
    print(get_used(key))

if __name__ == '__main__':
    main()
