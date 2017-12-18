import sys
from collections import defaultdict

class Computer:
    def __init__(self, instrs):
        self.last_play = None
        self.recover_q = []
        self.regs = defaultdict(int)
        self.pc = 0
        self.instrs = instrs
        self.ops = {
            'set': self._set_op,
            'add': self._add_op,
            'snd': self._snd_op,
            'mul': self._mul_op,
            'mod': self._mod_op,
            'rcv': self._rcv_op,
            'jgz': self._jgz_op,
        }

    def _int_or_reg(self, v):
        return self.regs[v] if v.isalpha() else int(v)

    def _set_op(self, X, Y):
        self.regs[X] = self._int_or_reg(Y)
        self.pc += 1

    def _add_op(self, X, Y):
        self.regs[X] += self._int_or_reg(Y)
        self.pc += 1

    def _snd_op(self, X):
        self.last_play = self._int_or_reg(X)
        self.pc += 1

    def _mul_op(self, X, Y):
        self.regs[X] *= self._int_or_reg(Y)
        self.pc += 1

    def _mod_op(self, X, Y):
        self.regs[X] %= self._int_or_reg(Y)
        self.pc += 1

    def _rcv_op(self, X):
        if self._int_or_reg(X):
            print(self.last_play)
            sys.exit()
            self.recover_q.append(self.last_play)
        self.pc += 1

    def _jgz_op(self, X, Y):
        if self._int_or_reg(X) > 0:
            self.pc += self._int_or_reg(Y)
        else:
            self.pc += 1

    def run(self):
        while 0 <= self.pc < len(self.instrs):
            cmd, *args = self.instrs[self.pc].split()
            self.ops[cmd](*args)


def main():
    instrs = []
    for line in sys.stdin.readlines():
        instrs.append(line.strip())

    computer = Computer(instrs)
    computer.run()


if __name__ == '__main__':
    main()
