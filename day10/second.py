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

def get_hex_repr(dense):
    h = ''
    for d in dense:
        d_hex = hex(d)[2:]
        h += '0' + d_hex if len(d_hex) == 1 else d_hex
    return h

def main():
    lengths = [ord(c) for c in input()] + SEED_LENS
    knots = do_rounds(list(range(LIST_SIZE)), lengths)
    dense = make_dense_hash(knots)
    print(get_hex_repr(dense))


if __name__ == '__main__':
    main()
