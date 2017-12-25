import sys
from collections import defaultdict

class State:
    @staticmethod
    def parse_state(lines):
        _, _, name = lines[1][:-1].split()
        _, _, _, _, zw = lines[3][:-1].split()
        _, _, _, _, _, _, zdir = lines[4][:-1].split()
        _, _, _, _, znext = lines[5][:-1].split()
        _, _, _, _, ow = lines[7][:-1].split()
        _, _, _, _, _, _, odir = lines[8][:-1].split()
        _, _, _, _, onext = lines[9][:-1].split()
        return State(name,
                     (int(zw), -1 if zdir == 'left' else 1, znext),
                     (int(ow), -1 if odir == 'left' else 1, onext))

    def __init__(self, name, zero, one):
        self.name = name
        self.move = [zero, one]

def checksum(tape):
    return sum(tape.values())

def simulate(states, st, iters):
    tape = defaultdict(int)
    tape_i = 0
    for _ in range(iters):
        tape[tape_i], d, st = states[st].move[tape[tape_i]]
        tape_i += d
    return checksum(tape)

def main():
    _, _, _, beginstate = input()[:-1].split()
    _, _, _, _, _, steps, _ = input().split()
    stateinput = [l.strip() for l in sys.stdin.readlines()]
    S = len(stateinput) // 10
    states = {}
    for i in range(S):
        s = State.parse_state(stateinput[i * 10:(i + 1) * 10])
        states[s.name] = s

    print(simulate(states, beginstate, int(steps)))
    

if __name__ == '__main__':
    main()
