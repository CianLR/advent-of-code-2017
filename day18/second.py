import sys
from collections import defaultdict

class PipeNoValueException(Exception):
    pass

class PipeDeadlockException(Exception):
    pass

class Pipe:
    def __init__(self):
        self.a_send_count = 0
        self.b_send_count = 0
        self.a_queue = []
        self.b_queue = []
        self.a_waiting = False
        self.b_waiting = False

    def is_deadlocked(self):
        return (self.a_waiting and not self.a_queue and
                self.b_waiting and not self.b_queue)

    def a_get(self):
        self.a_waiting = True
        if self.is_deadlocked():
            raise PipeDeadlockException()
        if not self.a_queue:
            raise PipeNoValueException()
        val, *self.a_queue = self.a_queue
        self.a_waiting = False
        return val

    def b_get(self):
        self.b_waiting = True
        if self.is_deadlocked():
            raise PipeDeadlockException()
        if not self.b_queue:
            raise PipeNoValueException()
        val, *self.b_queue = self.b_queue
        self.b_waiting = False
        return val

    def a_send(self, v):
        self.a_send_count += 1
        self.b_queue.append(v)

    def b_send(self, v):
        self.b_send_count += 1
        self.a_queue.append(v)


class Computer:

    YIELD = -1
    DONE = -2

    def __init__(self, instrs, process_id, pipe_get, pipe_send):
        self.instrs = instrs
        self.regs = defaultdict(int)
        self.regs['p'] = process_id
        self._pipe_get = pipe_get
        self._pipe_send = pipe_send
        self.pc = 0
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
        self._pipe_send(self._int_or_reg(X))
        self.pc += 1

    def _mul_op(self, X, Y):
        self.regs[X] *= self._int_or_reg(Y)
        self.pc += 1

    def _mod_op(self, X, Y):
        self.regs[X] %= self._int_or_reg(Y)
        self.pc += 1

    def _rcv_op(self, X):
        try:
            val = self._pipe_get()
        except PipeNoValueException:
            return Computer.YIELD
        self.regs[X] = val
        self.pc += 1

    def _jgz_op(self, X, Y):
        if self._int_or_reg(X) > 0:
            self.pc += self._int_or_reg(Y)
        else:
            self.pc += 1

    def run(self):
        while 0 <= self.pc < len(self.instrs):
            cmd, *args = self.instrs[self.pc].split()
            if self.ops[cmd](*args) == Computer.YIELD:
                return Computer.YIELD
        return Computer.DONE


def run_multi(instrs):
    p = Pipe()
    cmps = [
        Computer(instrs, 0, p.a_get, p.a_send),
        Computer(instrs, 1, p.b_get, p.b_send)
    ]
    is_done = {0: False, 1: False}
    cur = 0
    while True:
        try:
            exit_code = cmps[cur].run()
        except PipeDeadlockException:
            break
        if exit_code == Computer.DONE:
            is_done[cur] = True
        cur = 0 if cur else 1
        if is_done[cur]:
            break
    return p.b_send_count

def main():
    instrs = []
    for line in sys.stdin.readlines():
        instrs.append(line.strip())

    print(run_multi(instrs))

if __name__ == '__main__':
    main()
