import sys

CONVS = {
    'set': '{} = {};'.format,
    'sub': '{} -= {};'.format,
    'mul': '{} *= {}; ++muls;'.format,
}

lines = sys.stdin.readlines()

def convert(ln, cmd, x, y):
    if cmd == 'jnz':
        return 'if ({} != 0) goto line{};'.format(
                x, ln + int(y) if 0 <= ln + int(y) < len(lines) else 'end')
    return CONVS[cmd](x, y)

program = [
    'int main() {',
    'unsigned long muls = 0;',
    'long a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0;',
]
program_end = [
    'lineend:',
    'printf("%lu\\n", muls);',
    '}',
]

for ln, line in enumerate(lines):
    cmd, x, y = line.split()
    program.append('line{}: {}'.format(ln, convert(ln, cmd, x, y), ln))

print '\n'.join(program + program_end)
