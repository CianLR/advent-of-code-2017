import sys
import operator
from collections import defaultdict

OPS = {
    '<': operator.lt,
    '>': operator.gt,
    '==': operator.eq,
    '<=': operator.le,
    '>=': operator.ge,
    '!=': operator.ne,
}

class Instruction:
    def __init__(self, line, regs):
        self.regs = regs
        reg, direc, diff, _, cond_reg, op, cond_val = line.split()
        self.reg = reg
        self.diff = int(diff) if direc == 'inc' else -int(diff)
        self.cond = lambda: OPS[op](self.regs[cond_reg], int(cond_val))

    def exec(self):
        if self.cond():
            self.regs[self.reg] += self.diff
        

class CPU:
    def __init__(self, instrs):
        self.pc = 0
        self.regs = defaultdict(int)
        self.instrs = [Instruction(ins, self.regs) for ins in instrs]

    def run(self):
        max_max_reg = -10e9
        while 0 <= self.pc < len(self.instrs):
            self.instrs[self.pc].exec()
            self.pc += 1
            max_max_reg = max(max_max_reg, self.max_reg())
        return max_max_reg

    def max_reg(self):
        return max(self.regs.values())

def main():
    lines = []
    for line in sys.stdin.readlines():
        line = line.strip()
        lines.append(line)
    cpu = CPU(lines)
    print(cpu.run())

if __name__ == '__main__':
    main()
